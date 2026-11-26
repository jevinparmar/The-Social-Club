import os
from .base import *

# Default to development settings if not specified
env_name = os.getenv("ENVIRONMENT", "development").lower()

if env_name == "production":
    from .production import *
elif env_name == "testing":
    from .testing import *
else:
    from .development import *
