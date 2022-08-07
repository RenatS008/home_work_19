import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

from application.dao.user_dao import UserDAO
from application.dao.model.user import User


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_all(self) -> list[User]:
        return self.user_dao.get_all_users()

    def add_user(self, data):
        self.user_dao.create_user(**data)

    def update(self, data):
        self.user_dao.update_user(data)

    def delete(self, user_id):
        self.user_dao.delete(user_id)


def get_hash_for_user(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")
