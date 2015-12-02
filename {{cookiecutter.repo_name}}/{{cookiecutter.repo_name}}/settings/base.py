import sys
from os import environ
from os.path import join, abspath, dirname
from easy_thumbnails.conf import Settings as thumbnail_settings

# PATH vars
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)
SITE_ROOT = PROJECT_ROOT

sys.path.insert(0, root('apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = r"ll=&4)2zk&-2jy!o7j9#5dj+^b5=53vha1m-*o#x3rde%=@g=-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'djangobower',                    # django-bower
    'floppyforms',                    # django-floppyforms
    'django_extensions',              # django-extensions
    'ckeditor',                       # django-ckeditor-updated
    'easy_thumbnails',                # django-image-cropping
    'image_cropping',                 # django-image-cropping
    'rest_framework',                 # djangorestframework
    'multisitesutils',
    'magicbackup',
    'frontend',
    'magicthemes',
    'taggit',
)

CONTENT_APPS = (  #magic-content-apps
    'magicgallery',
    'magiccontent',
    'magiccontent.contrib.textimagecontent',
    'magiccontent.contrib.formattedtextimagecontent',
    'magiccontent.contrib.imagecontent',
    'magiccontent.contrib.iconcontent',
    'magiccontent.contrib.dividertextcontent',
    'magiccontent.contrib.background',
    'magiccontentnavigation',
)

PROJECT_APPS = (
    'core',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += CONTENT_APPS
INSTALLED_APPS += PROJECT_APPS

BOWER_INSTALLED_APPS = (
    'bootstrap#3.2.0',
    'jquery#1.11.3',
    'magnific-popup#1.0.0',
    'font-awesome-bower#~4.3.0',
    'html.sortable#~0.1.6',
    'classie#1.0.1',
    'modernizr#~2.8.3',
    'animate.css#3.2.0',
    'waypoints#3.0.1',
    'frontend-guide-utils#master',
    'dropzone#~4.0.1',
    'moment#>=2.5.0',
    'flexslider#2.5.0',
    'reset-css',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{{cookiecutter.repo_name}}_dev_db.sqlite3',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'  # 'Europe/London'

SITE_ID = environ.get('DJANGO_SITE_ID', 1)

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = root('assets', 'uploads')
MEDIA_URL = '/media/'

# Additional locations of static files

STATICFILES_DIRS = (
    root('assets'),
    root('frontend', 'static'),
)

TEMPLATE_DIRS = (
    root('templates'),
    root('frontend', 'templates'),
)

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = (
    root('frontend', 'static'),
)

# django-bower
BOWER_COMPONENTS_ROOT = root('components', )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'magicthemes.context_processors.frontend_processor',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# django-ckeditor-updated
CKEDITOR_UPLOAD_PATH = root('media', 'uploads')
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
             '-', 'Undo', 'Redo'],
            ['Find', ],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
             'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
             '-', 'Blockquote', '-', 'JustifyLeft',
             'JustifyCenter', 'JustifyRight', 'JustifyBlock', ],
            ['Link', 'Unlink', 'Anchor'],
            ['Table', 'HorizontalRule', 'Smiley',
             'SpecialChar', 'PageBreak', 'Iframe'],  # 'Image'
            ['Format', 'Font', 'FontSize'],  # 'Styles'
            ['TextColor', 'BGColor'],
            ['ShowBlocks', '-'],  # 'Maximize'
            # ['Source', ],
        ],
        'height': 380,
        'width': '100%',
        'uiColor': '#FFFCFC',
        'autoGrow_onStartup': True,
    },
    'simple': {
        'toolbar': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
             'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', ],
            ['Link', 'Unlink', 'Anchor'],
            ['Format', 'FontSize'],
            ['ShowBlocks', '-'],
        ],
        'height': 180,
        'width': '100%',
    },
}

# django-image-cropping
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# django-magic-gallery
GALLERY_PAGE_IS_OWNER_METHOD = 'core.views.is_the_site_owner'

# django-magic-content
MAGICCONTENT_CAN_EDIT_METHOD = 'core.views.is_the_site_owner'
REGISTER_LINKS = [
    {'model': 'magiccontent.Area', 'skip_instance_rule': r'_\d+'},
    {'full_reverse_link': {'url': 'galleries.gallery.list',
                           'name': 'Galleries'}},
    {'model': 'magicgallery.Gallery'},
]

# django-magic-backup
BACKUP_TARGET_DIR = root('backups', )

# .local.py overrides all the common settings.
try:
    from .local import *
except ImportError:
    pass


# importing test settings file if necessary
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    from .testing import *
