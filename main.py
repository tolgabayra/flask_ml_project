from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from controller.user_controller import user_controller
from controller.auth_controller import auth_controller
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432'
    app.config.from_object(config_class)
    app.run(port=5000)
    db.init_app(app)
    # cors
    CORS(app)
    app.register_blueprint(auth_controller, url_prefix='/api/v1')
    app.register_blueprint(user_controller, url_prefix='/api/v1')

    return app


# kod bloğu, bir Python dosyasının başka bir dosya tarafından modül olarak kullanılmayıp, doğrudan çalıştırılması
# durumunda yürütülecek kodları içeren bir yapıdır.
if __name__ == '__main__':
    create_app()
