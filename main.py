from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller.user_controller import user_controller
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_controller, url_prefix='/api/v1')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432'
    app.run(port=5000)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    create_app()
