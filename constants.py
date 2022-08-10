import base64
from hashlib import pbkdf2_hmac

SECRET_KEY = '798d8a85fda4a26bf92ee'
PWD_HASH_SALT = base64.b16decode
PWD_HASH_ITERATIONS = 100_000
ALGORITHMS = pbkdf2_hmac
TOKEN_EXPIRE_MINUTES = 15
TOKEN_EXPIRE_DAYS = 130
HASH_NAME = "sha256"
