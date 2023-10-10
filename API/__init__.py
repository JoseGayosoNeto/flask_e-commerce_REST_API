from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import pymysql, logging
from logging.handlers import RotatingFileHandler



pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)

api = Api(app)

# Adicionando log em um arquivo
log_file = 'app.log'
log_formatter = formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = RotatingFileHandler(log_file, maxBytes= 1024*1024*8,backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(log_formatter)
app.logger.addHandler(file_handler)

from .views import product_views
from .models import product_model
