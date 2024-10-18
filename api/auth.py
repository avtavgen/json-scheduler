from ninja.security import HttpBearer

from JsonScheduler.settings import SUPERSECRET


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == SUPERSECRET:
            return token