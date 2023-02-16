from model import User
from util.helper import Helper
from typing import Optional
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AuthService:

    @staticmethod
    def login(email: str, password: str) -> Optional[str]:
        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            return None

        access_token = Helper.generate_access_token(user.id)
        return access_token

    @staticmethod
    def register(name, email, password):
        hashed_password = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user
