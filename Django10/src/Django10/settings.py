"""
Django settings for Django10 project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls.base import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#LOGIN_URL : login_require 데코레이터/ LoginRequiredMixin 클래스를 통해
#비로그인 회원이 이동할 로그인 페이지의 주소
LOGIN_URL = reverse_lazy('cl:signin')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zwylsi9=(z#il=m36cit_rnqpb57)2&5lg+8ljif$5ozj!7=&-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','pythonanywhere.com']

#인증 관련 모듈을 추가하는 변수
AUTHENTICATION_BACKENDS =(
    #구글 인증관련 처리 클래스 추가
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    #소셜로그인 정보를 Django의 User모델클래스에 매칭
    'django.contrib.auth.backends.ModelBackend',
    )

#구글계정에서 할당받은 ID, PASSWORD 저장
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='155822568736-niuuiftra7p84jaukfbs8qftu14qh3m1.apps.googleusercontent.com'     #ID값 저장
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'F5CX0VLn3ScBaqd_wEpxmwZu'#보안비밀 값 저장

# Application definition

#INSTALLED_APPS : 해당 프로젝트에서 사용할 어플리케이션명을 저장하는 변수
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark', #새로 추가한 어플리케이션을 프로젝트에 등록하는 과정
    'vote',     #투표어플리케이션 
    'customlogin',#회원관리 어플리케이션
    #python에 social-auth-app-django 모듈이 설치되야함
    'social_django', #소셜로그인에 관련된 처리를 하는 어플리케이션
    'blog'
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

ROOT_URLCONF = 'Django10.urls'

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
                #소셜로그인을 처리하기위한 템플릿관련 함수 추가
                'social_django.context_processors.backends',#
                'social_django.context_processors.login_redirect',#
            ],
        },
    },
]

WSGI_APPLICATION = 'Django10.wsgi.application'


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

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#URL 주소로 파일 주소를 접근할 때 사용하는 변수
#http://127.0.0.1:8000/files/ 로 시작하는 경로는 미디어파일을 불러오는 것으로 판단
MEDIA_URL = '/files/'
#실제로 파일들을 저장하는 경로  MEDIA_ROOT = 'c:/files/'
#os.path.join(기존경로, 새경로) : 기존경로에 새경로를 붙인 문자열 반환
#BASE_DIR : 웹서버가 존재하는 경로
#django10/src/files/ 경로에 파일들을 실제로 저장하도록 설정
MEDIA_ROOT = os.path.join(BASE_DIR,'files')





