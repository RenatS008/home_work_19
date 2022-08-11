import base64
import os


class Config(object):
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'movies.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = '798d8a85fda4a26bf92ee'
    ALGORITHM = 'HS256'
    PWD_HASH_ITERATIONS = 1000000
    PWD_HASH_SALT = base64.b64decode("salt")

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130
