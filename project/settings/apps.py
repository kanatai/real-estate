# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Required for GraphiQL

    # libraries
    'rest_framework',
    'rest_framework.authtoken',

    'corsheaders',
    'drf_yasg',
    'django_filters',
    'django_extensions',

    # my apps
    'apps.user',
    'apps.apartments',
    'apps.favorite',
    'apps.region',
    'apps.services',
    'apps.banner'
]
