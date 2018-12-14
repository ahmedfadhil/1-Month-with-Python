from pipestack.pipe import Marble, MarblePipe
from conversionkit import Field
from stringconvert import unicodeToUnicode
import logging

log = logging.getLogger(__name__)

class SimpleUserMarble(Marble):
    def user_has_password(self, username, password):
        if username == self.config.username and \
           password == self.config.password:
            return True
        else:
            return False

class SimpleUserPipe(MarblePipe):
    options = {
        'username': Field(
            unicodeToUnicode(), 
            missing_or_empty_error='No %(name)s.username specified',
        ),
        'password': Field(
            unicodeToUnicode(), 
            missing_or_empty_error='No %(name)s.password specified',
        ),
    }
    marble_class = SimpleUserMarble

