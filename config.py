import os

import constants


class Config(object):
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'movies.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = constants.SECRET_KEY
    HASH_NAME = constants.HASH_NAME
    ALGORITHMS = constants.ALGORITHMS

    PWD_HASH_SALT = constants.PWD_HASH_SALT
    PWD_HASH_ITERATIONS = constants.PWD_HASH_ITERATIONS

    TOKEN_EXPIRE_MINUTES = constants.TOKEN_EXPIRE_MINUTES
    TOKEN_EXPIRE_DAYS = constants.TOKEN_EXPIRE_DAYS



