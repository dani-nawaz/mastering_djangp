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
AUTH_USER_MODEL = 'blango_auth.User'

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "blog.api.throttling.AnonSustainedThrottle",
        "blog.api.throttling.AnonBurstThrottle",
        "blog.api.throttling.UserSustainedThrottle",
        "blog.api.throttling.UserBurstThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon_sustained": "500/day",
        "anon_burst": "10/minute",
        "user_sustained": "5000/day",
        "user_burst": "100/minute",
        "post_api": "50/minute",
        "user_api": "2000/day"
    },
}
