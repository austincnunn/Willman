import os
from pathlib import Path

basedir = Path(__file__).parent.absolute()


APP_VERSION = '0.15.0'
RELEASE_CHANNEL = os.environ.get('RELEASE_CHANNEL', 'stable')
GIT_SHA = os.environ.get('GIT_SHA', '')[:7]  # Short SHA
GITHUB_REPO = 'austincnunn/may'
BOOTSTRAP_CSS_ASSET_URL = os.environ.get('BOOTSTRAP_CSS_ASSET_URL', '/static/vendor/bootstrap.min.css')
BOOTSTRAP_CSS_CDN_URL = os.environ.get('BOOTSTRAP_CSS_CDN_URL', 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css')
BOOTSTRAP_JS_ASSET_URL = os.environ.get('BOOTSTRAP_JS_ASSET_URL', '/static/vendor/bootstrap.bundle.min.js')
BOOTSTRAP_JS_CDN_URL = os.environ.get('BOOTSTRAP_JS_CDN_URL', 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js')
JQUERY_ASSET_URL = os.environ.get('JQUERY_ASSET_URL', '/static/vendor/jquery.min.js')
JQUERY_CDN_URL = os.environ.get('JQUERY_CDN_URL', 'https://code.jquery.com/jquery-3.7.1.min.js')
JQUERYUI_JS_ASSET_URL = os.environ.get('JQUERYUI_JS_ASSET_URL', '/static/vendor/jquery-ui.min.js')
JQUERYUI_JS_CDN_URL = os.environ.get('JQUERYUI_JS_CDN_URL', 'https://code.jquery.com/ui/1.14.1/jquery-ui.min.js')
JQUERYUI_CSS_ASSET_URL = os.environ.get('JQUERYUI_CSS_ASSET_URL', '/static/vendor/jquery-ui.min.css')
JQUERYUI_CSS_CDN_URL = os.environ.get('JQUERYUI_CSS_CDN_URL', 'https://code.jquery.com/ui/1.14.1/themes/base/jquery-ui.min.css')

# Build display version (e.g., "0.5.0" for stable, "0.5.0-dev+abc1234" for dev)
if RELEASE_CHANNEL == 'dev' and GIT_SHA:
    DISPLAY_VERSION = f"{APP_VERSION}-dev+{GIT_SHA}"
elif RELEASE_CHANNEL == 'dev':
    DISPLAY_VERSION = f"{APP_VERSION}-dev"
else:
    DISPLAY_VERSION = APP_VERSION


class Config:
    APP_VERSION = APP_VERSION
    DISPLAY_VERSION = DISPLAY_VERSION
    RELEASE_CHANNEL = RELEASE_CHANNEL
    GIT_SHA = GIT_SHA
    GITHUB_REPO = GITHUB_REPO
    BOOTSTRAP_CSS_ASSET_URL = BOOTSTRAP_CSS_ASSET_URL
    BOOTSTRAP_CSS_CDN_URL = BOOTSTRAP_CSS_CDN_URL
    BOOTSTRAP_JS_ASSET_URL = BOOTSTRAP_JS_ASSET_URL
    BOOTSTRAP_JS_CDN_URL = BOOTSTRAP_JS_CDN_URL
    JQUERY_ASSET_URL = JQUERY_ASSET_URL
    JQUERY_CDN_URL = JQUERY_CDN_URL
    JQUERYUI_JS_ASSET_URL = JQUERYUI_JS_ASSET_URL
    JQUERYUI_JS_CDN_URL = JQUERYUI_JS_CDN_URL
    JQUERYUI_CSS_ASSET_URL = JQUERYUI_CSS_ASSET_URL
    JQUERYUI_CSS_CDN_URL = JQUERYUI_CSS_CDN_URL
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        import secrets
        # Generate a random key for development, but warn about it
        SECRET_KEY = secrets.token_hex(32)
        import warnings
        warnings.warn(
            "SECRET_KEY environment variable not set. Using randomly generated key. "
            "Sessions will not persist across restarts. Set SECRET_KEY for production.",
            RuntimeWarning
        )
    INTERNAL_API_KEY = os.environ.get('INTERNAL_API_KEY') or __import__('secrets').token_hex(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{basedir}/data/willman.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or str(basedir / 'data' / 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
