# REST_FRAMEWORK
REST_FRAMEWORK = {
    # Use Django's standard `django_back.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DATE_FORMAT': "%Y-%m-%d",
    'DATE_INPUT_FORMATS': ["%m/%d/%Y", "%m-%d-%Y", "%Y-%m-%d"],
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    'DATETIME_INPUT_FORMATS': ["%Y-%m-%d %H:%M:%S"],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DATA_UPLOAD_MAX_MEMORY_SIZE': (10 * 1024 * 1024),  # Например, 5 MB (5 * 1024 * 1024)
}
