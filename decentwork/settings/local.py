from .base import *

DEBUG = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'local')
]

INSTALLED_APPS += ('debug_toolbar',)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

VALIDATE_FRONT_PASSWORD = False

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE

INTERNAL_IPS = [
    '0.0.0.0',
    '127.0.0.1'
]

# Determines if verification email is send
# 'mandatory' - email is send user cant login without verification
# 'optional' - email is send user can login without verification
# 'none' - email is not send
ACCOUNT_EMAIL_VERIFICATION = 'none'

WEBPACK_MANIFEST_FILE = {
    'FILE': os.path.join(BASE_DIR, './../manifest-local.json'),
}

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures', 'dev'),
    os.path.join(BASE_DIR, 'fixtures', 'tests')
]
