from .base import *
from .apps import *
from .middleware import *
from .databases import *
from .parameters import *
from .email import *
from .rest_framework import *

# you need to set "env = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ.get('env') == 'prod':
    from .prod import *
else:
    from .dev import *

# CORS
CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_ALLOW_CREDENTIALS = DEBUG
