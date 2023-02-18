from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from controller.user_controller import user_controller
from controller.auth_controller import auth_controller
from config import Config
from model import db



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/postgres'
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    # cors
    CORS(app)
    app.register_blueprint(auth_controller, url_prefix='/api/v1')
    app.register_blueprint(user_controller, url_prefix='/api/v1')
    return app


# kod bloğu, bir Python dosyasının başka bir dosya tarafından modül olarak kullanılmayıp, doğrudan çalıştırılması
# durumunda yürütülecek kodları içeren bir yapıdır.
if __name__ == '__main__':
    my_app = create_app()
    my_app.run(port=5000)

# if __name__ == '__main__':
#     my_app = create_app()
#     with my_app.app_context():
#         db.create_all()
#     my_app.run(port=5000)
