import base64
from hashlib import pbkdf2_hmac

SECRET_KEY = '798d8a85fda4a26bf92ee29485dac839e21a7e2d27403be263ba0c94729faa0fd' \
             'd710c078a8b0f82d0aae741b5e907e3fb3543046b07a5a11e75b6a96ad0438b '
PWD_HASH_SALT = base64.b16decode("salt")
PWD_HASH_ITERATIONS = 100_000
ALGORITHM = pbkdf2_hmac
TOKEN_EXPIRE_MINUTES = 15
TOKEN_EXPIRE_DAYS = 187200
