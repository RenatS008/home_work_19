import os

import constants


class Config(object):
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'movies.db')
    PWD_HASH_SALT = constants.PWD_HASH_SALT
    PWD_HASH_ITERATIONS = constants.PWD_HASH_ITERATIONS
    ALGORITHM = constants.ALGORITHM
    SECRET_KEY = constants.SECRET_KEY
    TOKEN_EXPIRE_MINUTES = constants.TOKEN_EXPIRE_MINUTES
    TOKEN_EXPIRE_DAYS = constants.TOKEN_EXPIRE_DAYS
