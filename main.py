from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller.user_controller import user_controller
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432'
    app.config.from_object(config_class)
    app.run(port=5000)
    db.init_app(app)

    app.register_blueprint(user_controller, url_prefix='/api/v1')


    return app


if __name__ == '__main__':
    create_app()
