import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=05ci$q@zl%qc0^000-v#hh^a-)!i6#6m=o7f8+!qyi8fal^8@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'delivery',
    'imageboard',
    'main',
    'user',
    'ckeditor',
    'ckeditor_uploader',
    'hitcount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TPNU.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TPNU.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')

STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC')

STATIC_URL = '/static/'
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'board', 'static'),
    os.path.join(BASE_DIR, 'delivery', 'static'),
    os.path.join(BASE_DIR, 'imageboard', 'static'),
    os.path.join(BASE_DIR, 'main', 'static'),
    os.path.join(BASE_DIR, 'user', 'static'),
]
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     # 'django.contrib.staticfiles.finders.AppDirectoriesFinder',    #causes verbose duplicate notifications in django 1.9
# ) 그냥 STATIC rm하고 이거 끄고 collecstatic하자
# Media files 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'MEDIA')



# email authentication

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

EMAIL_HOST = "smtp.gmail.com"
# 메일을 호스트하는 서버
EMAIL_PORT = "587"
# gmail과의 통신하는 포트
EMAIL_HOST_USER = "gt03051@gmail.com"
# 발신할 이메일
EMAIL_HOST_PASSWORD = "16331541z"
# 발신할 메일의 비밀번호
EMAIL_USE_TLS = True
# TLS 보안 방법
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# 사이트와 관련한 자동응답을 받을 이메일 주소,'webmaster@localhost'


CORS_ORIGIN_ALLOW_ALL = True


#cheditor

CKEDITOR_UPLOAD_PATH = "uploads/"

AWS_QUERYSTRING_AUTH = False

CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
