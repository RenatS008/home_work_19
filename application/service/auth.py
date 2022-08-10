import base64
import calendar
import hashlib
import datetime

import jwt
from config import Config


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name=Config["HASH_NAME"],
        password=password.encode("utf-8"),
        salt=Config["PWD_HASH_SALT"],
        iterations=Config["PWD_HASH_ITERATIONS"]
    )


def generate_hash_for_password(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compare_pass_and_hash(password_hash, other_password) -> bool:
    return password_hash == generate_hash_for_password(other_password)


def generate_token_for_user(username, password, password_hash, is_refresh=False):
    if username is None:
        return None

    if not is_refresh:
        if not compare_pass_and_hash(password_hash=password_hash, other_password=password):
            return None

    data = {
        "username": username,
        "password": password,
    }

    # 30 MIN FOR ACCESS_TOKEN
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=Config['TOKEN_EXPIRE_MINUTES'])
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, secret=Config['SECRET_KEY'],
                              algorithm=Config['ALGORITHM'])

    # 130 DAYS FOR ACCESS_TOKEN
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=Config['TOKEN_EXPIRE_DAYS'])
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, secret=Config['SECRET_KEY'],
                               algorithm=Config['ALGORITHM'])

    token = {"access_token": access_token,
             "refresh_token": refresh_token
             }

    return token, 201


def check_token(token):
    data = jwt.decode(token, secret=Config['ALGORITHM'],
                      algorithms=Config['ALGORITHM'])

    username = data.get('username')
    password = data.get('password')
    return generate_token_for_user(username=username,
                                   password=password,
                                   password_hash=None,
                                   is_refresh=True
                                   )
