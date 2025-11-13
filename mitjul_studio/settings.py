"""
Django settings for mitjul_studio project.
"""

from pathlib import Path
import os
import dj_database_url # Render 배포 환경 변수 처리를 위해 추가

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------
# 1. SECURITY SETTINGS
# --------------------

# SECURITY WARNING: keep the secret key used in production secret!
# 실제로는 os.environ.get('SECRET_KEY')로 안전하게 관리해야 합니다.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-anb@-maqdx8olmr1t5(mz7dq)vg*=nd2w8ffed24&2yn7&fc^m')

# SECURITY WARNING: don't run with debug turned on in production!
# Render 환경에서는 DEBUG=False로 설정해야 합니다.
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'


# ALLOWED_HOSTS: Render URL과 로컬 주소를 포함하여 400 Bad Request 방지
ALLOWED_HOSTS = [
    'mitjul-studio.onrender.com', 
    'www.당신의도메인.com', 
    '당신의도메인.com', 
    '127.0.0.1', 
    'localhost',
    'testserver', # 테스트 환경용
]


# --------------------
# 2. APPLICATION DEFINITION
# --------------------

INSTALLED_APPS = [
    # 기본 앱들
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mongoengine', # MongoDB (MongoEngine) 지원
    
    # 사용자 앱
    'core', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # Whitenoise 추가
]

ROOT_URLCONF = 'mitjul_studio.urls'

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

WSGI_APPLICATION = 'mitjul_studio.wsgi.application'

# --------------------
# 3. DATABASE SETTINGS (SQLite + MongoDB)
# --------------------

# MongoDB URI: Render 환경 변수 MONGODB_URI를 사용하도록 설정
MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/mitjul_studio_db')

# MongoEngine 설정
MONGODB_DATABASES = {
    'default': {
        # 'name'은 URI에서 자동으로 추출될 수 있으나 명시적으로 설정
        'name': MONGODB_URI.split('/')[-1].split('?')[0] if 'mongodb' in MONGODB_URI else 'mitjul_studio_db',
        'host': MONGODB_URI, 
    }
}

# SQLite (Auth, Admin 등 Django 기본 기능용)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', 
    }
}

# --------------------
# 4. STATIC FILES (CSS, JS, Images)
# --------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # 정적 파일을 모을 최종 디렉토리 (배포용)

# STATICFILES_DIRS: Django가 정적 파일을 찾을 원본 폴더 (core/static)
STATICFILES_DIRS = [
    BASE_DIR / "core" / "static",
]

# **[Critical Fix]** Render 배포 성공을 위해 whitenoise 설정을 STATICFILES_STORAGE 방식으로 명시
# 이전 STORAGES 블록 대신 이 코드를 사용합니다.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" 

# Media files (사용자 업로드 파일)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# --------------------
# 5. GENERAL SETTINGS
# --------------------

# Password validation (생략)
AUTH_PASSWORD_VALIDATORS = [
    # ... (기존 내용 유지)
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
LANGUAGE_CODE = 'ko-kr' # 한국어 설정으로 변경 (선택 사항)
TIME_ZONE = 'Asia/Seoul' # 한국 시간대로 변경 (선택 사항)

USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'