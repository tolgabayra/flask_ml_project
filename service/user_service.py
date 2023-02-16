from model import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserService:
    #     @staticmethod
    #     def create_user(user_dto: UserCreateDTO):
    #         user = User(name=user_dto.name, email=user_dto.email)
    #         db.session.add(user)
    #         db.session.commit()
    #         return user

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
    def update_user(id, data):
        record = User.query.get(id)
        if record:
            for key, value in data.items():
                setattr(record,key,value)
                db.session.commit()
                return True
        else:
            return False

    @staticmethod
    def show_user(id):
        return User.query.get(id)

    @staticmethod
    def list_user():
        return User.query.all()
