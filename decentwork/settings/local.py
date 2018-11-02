from .base import *

DEBUG = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'local')
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats.local.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

INSTALLED_APPS += ('debug_toolbar',)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

VALIDATE_FRONT_PASSWORD = False

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE

# Determines if verification email is send
# 'mandatory' - email is send user cant login without verification
# 'optional' - email is send user can login without verification
# 'none' - email is not send
ACCOUNT_EMAIL_VERIFICATION = 'none'
