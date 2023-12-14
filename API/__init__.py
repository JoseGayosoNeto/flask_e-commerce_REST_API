from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import pymysql, logging
from logging.handlers import RotatingFileHandler
from flask_jwt_extended import JWTManager



pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)

api = Api(app)

jwt = JWTManager(app)

log_file = 'app.log'
logging.basicConfig(filename=log_file, format='%(asctime)s - %(levelname)s - %(threadName)s - %(message)s', level=logging.DEBUG)


from .views import product_views, cart_views, user_views, login_views, refresh_token_views
from .models import product_model, cart_model, user_model
