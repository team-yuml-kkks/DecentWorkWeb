from .base import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'dist')

# Determines if verification email is send
# 'mandatory' - email is send user cant login without verification
# 'optional' - email is send user can login without verification
# 'none' - email is not send
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

WEBPACK_MANIFEST_FILE = {
    'FILE': os.path.join(BASE_DIR, './../manifest-dist.json'),
}
