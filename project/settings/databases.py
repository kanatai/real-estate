# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import os

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME', 'real-estate'),
            'USER': os.environ.get('DB_USER', 'real-estate'),
            'PASSWORD': os.environ.get('DB_PASSWORD', '123qwe'),
            'HOST': os.environ.get('DB_HOST', 'db'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
}
#pstgres нужно запихнуть в гитигнор