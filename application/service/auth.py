import base64
import calendar
import hashlib
import datetime

import jwt
from flask import current_app


def generate_pass_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"]
    )


def pass_encoded_to_hash(password: str) -> str:
    return base64.b64encode(generate_pass_digest(password)).decode('utf-8')


def compare_pass_and_hash(password_hash, other_password) -> bool:
    return password_hash == other_password


def generate_token_for_user(username, password, password_hash, is_refresh=False):
    if username is None:
        return None
    if not is_refresh:
        if compare_pass_and_hash(password_hash=password_hash, other_password=password):
            return None

    data = {
        "username": username,
        "password": password
    }

    # 30 MIN FOR ACCESS_TOKEN
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, secret=current_app.config['SECRET_KEY'],
                              algorithm=current_app.config['ALGORITHM'])

    # 130 DAYS FOR ACCESS_TOKEN
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, secret=current_app.config['SECRET_KEY'],
                               algorithm=current_app.config['ALGORITHM'])

    token = {"access_token": access_token,
             "refresh_token": refresh_token
             }

    return token, 201


def check_token(token):
    try:
        result = jwt.decode(token, secret=current_app.config['ALGORITHM'],
                            algorithm=current_app.config['ALGORITHM'])

        username = result.get('username')
        password = result.get('password')

        return generate_token_for_user(username=username,
                                       password=password,
                                       password_hash=None,
                                       is_refresh=True
                                       )
    except Exception as e:
        return False
