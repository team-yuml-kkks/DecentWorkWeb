from .base import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'dist')

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats.dist.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

# Determines if verification email is send
# 'mandatory' - email is send user cant login without verification
# 'optional' - email is send user can login without verification
# 'none' - email is not send
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
