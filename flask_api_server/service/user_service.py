from model import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserService:

    @staticmethod
    def create_user(name: str, email: str):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(id):
        record = User.query.get(id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def show_user(id):
        return User.query.get(id)

    @staticmethod
    def list_user(self):
        return User.query.all()
