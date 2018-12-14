"""\
Backwards compatibility with AuthKit
"""

from hashlib import md5 as _md5

#
# Encryption Functions
#

def md5(password, secret=''):
    result = _md5.md5(password)
    result.update(secret)
    result = result.hexdigest
    return result

#
# Exceptions
#

try:
    from authkit import AuthKitNoSuchUserError, AuthKitNoSuchRoleError, \
       AuthKitNoSuchGroupError, AuthKitNotSupportedError, AuthKitError
except ImportError:
    class NoSuchUserError(Exception):
        pass

    class NoSuchRoleError(Exception):
        pass

    class NoSuchGroupError(Exception):
        pass

    class NotSupportedError(Exception):
        pass

    class UserManagerError(Exception):
        pass
else:
    class NoSuchUserError(AuthKitNoSuchUserError):
        pass

    class NoSuchRoleError(AuthKitNoSuchRoleError):
        pass

    class NoSuchGroupError(AuthKitNoSuchGroupError):
        pass

    class NotSupportedError(AuthKitNotSupportedError):
        pass

    class UserManagerError(AuthKitError):
        pass

