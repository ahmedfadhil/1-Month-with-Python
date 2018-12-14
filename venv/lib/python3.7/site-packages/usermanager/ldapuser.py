import ldap
from pipestack.pipe import Marble, MarblePipe
from pipestack.ensure import ensure_method_bag, ensure_self_marble
from conversionkit import Field, toDictionary
from recordconvert import toListOfRecords
from stringconvert import unicodeToUnicode, unicodeToBoolean
from databasepipe.setup import BaseSetupCmd
import logging

log = logging.getLogger(__name__)

def listOfUsernames(split_name=False, extract_organisation=False):
    def listOfUsernames_converter(conversion, state=None):
        try:
            conversion.result = [
                v.strip() for v in conversion.value.split(',')
            ]
        except:
            conversion.error = (
                'Could not parse comma separated list of '
                'strings'
            )
    return listOfUsernames_converter

bypass_user = toListOfRecords(
     toDictionary(
         converters = {
             'username': Field(
                unicodeToUnicode(), 
                missing_or_empty_default=None,
             ),
             'password': Field(
                unicodeToUnicode(), 
                missing_or_empty_default=None,
             ),
         }
    )
)

class SetupCmd(BaseSetupCmd):

    table_names_string = 'authkit_login'

    @ensure_method_bag('database')
    def create_tables(self, bag):
        sql = """
            CREATE TABLE authkit_login (
                uid INTEGER PRIMARY KEY
              , user_username TEXT NOT NULL
              , login_time TEXT NOT NULL DEFAULT (datetime('now'))
              , login_ip text NOT NULL
            );
        """
        bag[self.aliases['database']].query(sql, fetch=False)

    @ensure_method_bag('database')
    def drop_tables(self, bag):
        sql = """
            DROP TABLE IF EXISTS authkit_login;
        """
        bag[self.aliases['database']].query(sql, fetch=False)
    
class LdapUserMarble(Marble):

    @ensure_self_marble('database')
    def all_login_records(marble):
        database = marble.bag[marble.aliases['database']]
        return database.query(
            """
            SELECT * FROM authkit_login;
            """,
        )
    
    @ensure_self_marble('database')
    def logged_in(marble, username, ip):
        if marble.config['log_logins']: 
            database = marble.bag[marble.aliases['database']]
            database.insert_record(
                "authkit_login",
                dict(login_ip=ip, user_username=username),
                "uid",
            )
    
    def user_has_password(marble, username, password):
        if marble.config.bypass_user:
            for user in marble.config.bypass_user:
                if username == user.username and password == user.password:
                    return True
        if marble.config.restrict_ldap_usernames and \
           username not in marble.config.restrict_ldap_usernames:
            log.debug(
                '%r is not one of the allowed LDAP usernames', 
                username
            )
            return False
        try:
            l = ldap.open(marble.config.server)
            bind_dn = marble.config.bind_dn%{'user_id':username}
            log.debug(
                "Binding %s %s %s...", 
                marble.config.server,
                bind_dn, 
                password,
            )
            l.simple_bind_s(bind_dn, password)
        except Exception, e:
            log.error("LDAP bind failed: %r", e)
            return False
        else:
            return True

class LdapUserPipe(MarblePipe):
    options = {
        'server': Field(
            unicodeToUnicode(), 
            missing_or_empty_error=(
                "Please enter the hostname or IP of the LDAP server in "
                "'%(name)s.server'"
            ),
        ),
        'bind_dn': Field(
            unicodeToUnicode(), 
            empty_error=(
                "Please enter the DN which should be used for binding users "
                "in the '%(name)s.bind_dn option; any strings '%%(user_id)s'"
                "in the string you enter will be replaced with the username "
                "of the user trying to sign in'",
            ),
            missing_default=False,
        ),
        'bypass_user': bypass_user,
        'restrict_ldap_usernames': Field(
            listOfUsernames(), 
            missing_or_empty_default=None,
        ),
        'log_logins': Field(
            unicodeToBoolean(), 
            missing_or_empty_default=None,
        ),
    }
    marble_class = LdapUserMarble

