import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
MAX_CONTENT_LENGTH = int(eval(os.environ.get('MAX_CONTENT_LENGTH')))
CACHE_TYPE = os.environ.get('CACHE_TYPE')
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')



USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
SERVER = 'localhost'
DB = os.environ.get('DB')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')