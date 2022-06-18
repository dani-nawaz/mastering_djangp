import random

from rest_framework import throttling


class AnonSustainedThrottle(throttling.AnonRateThrottle):
    scope = "anon_sustained"


class AnonBurstThrottle(throttling.AnonRateThrottle):
    scope = "anon_burst"


class UserSustainedThrottle(throttling.UserRateThrottle):
    scope = "user_sustained"


class UserBurstThrottle(throttling.UserRateThrottle):
    scope = "user_burst"


class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1
