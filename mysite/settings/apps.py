# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    "blango_auth",
    'books',
    'rest_framework',
    "drones.apps.DronesConfig",
    # "drones",
    "drf_yasg",
    'rest_framework.authtoken',
]

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
        "Basic": {"type": "basic"},
    }
}