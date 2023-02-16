import jwt
import hashlib
import os
from datetime import datetime, timedelta, timezone


class Helper:

    @staticmethod
    def generate_access_token(payload):
        return jwt.encode(
            {"some": payload, "exp": os.getenv("JWT_ACCESS_TOKEN_EXPIRES")},
            "secret_key", algorithm="HS256")

    @staticmethod
    def generate_refresh_token(payload):
        return jwt.encode({"some": payload}, "secrwt_key", algorithm="HS256")

    @staticmethod
    def generate_hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
