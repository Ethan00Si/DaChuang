"""
Django settings for DaChuang project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b^!3uco7i)kkk8rlt4+g^ma)9xq+1=)#r6t+p07)26qh=lg7-*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'get_openid',
    'userinfo',
    'userlog',
    # 注册新的app
    'recommender.apps.RecommenderConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.cache.FetchFromCacheMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DaChuang.urls'

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

WSGI_APPLICATION = 'DaChuang.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        
        # USER for mysql
        'USER':'root',

        # PASSWORD for mysql
        'PASSWORD':'',

        # NAME of DATABASE
        'NAME':'dachuang',

        # If this value starts with a forward slash ('/') and you’re using MySQL, MySQL will connect via a Unix socket to the specified socket. For example:
        # https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-NAME
        # '' means localhost
        'HOST':'localhost',
    }
}

# 内存cache,允许跨进程
'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
'''

# 数据库cache，支持跨进程，同时可以复用
'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        
        # LOCATION为一个不存在数据库中的数据表
        'LOCATION': 'my_cache_table',
    }
}
'''

# 文件cache，同上，跨进程，可复用

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    
        # LOCATION为数据缓存的绝对路径，此路径必须存在且可读可写，最后加不加斜杠无所谓
        'LOCATION': 'd:/Data/cache',

        # 一些设置
        # cache过期的时限(s)
        'TIMEOUT': 100,

        #传递给cache后端的参数
        'OPTIONS':{
            # 最多存多少个cache
            'MAX_ENTRIES': 1000,
            # cache数达到最大之后删去旧cache的比例，默认为 1/CULL_FREQUENCY
            'CULL_FREQUENCY': 3,
            # 每个cache后端都会有独特的设置，这些我觉得不重要
        }
        
    }
}


# Local-memory cache,不允许跨进程，但我试了在两个阅览器打开，我感觉是支持的。。。不知道有什么区别
'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        
        # 如果有多个Local-memory cache那么LOCATION为其独特的名字，如果只有一个可以忽略
        'LOCATION': '',
    }
}
'''
# 以下是基本的cache设置
# cache的连接名，在cache middleware中引用
CACHE_MIDDLEWARE_ALIAS  = 'default'

# 每一页会被cache保存多久(s)
CACHE_MIDDLEWARE_SECONDS = 600

# 如果同一个cache被多个网页分享，那么将其设置为网页名或者独特的字符，以防冲突
# 默认情况下为空
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# set to Chinese TIMEZONE
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
