from application.service.auth import generate_hash_for_password

from application.dao.user_dao import UserDAO
from application.dao.model.user import User


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_all(self) -> list[User]:
        return self.user_dao.get_all()

    def get_by_id(self, user_id):
        return self.user_dao.get_by_id(user_id)

    def get_by_username(self, username):
        return self.user_dao.get_by_username(username)

    def create(self, data) -> None:
        data["password"] = generate_hash_for_password(password=data["password"])
        return self.user_dao.create(data)

    def update(self, data) -> None:
        return self.user_dao.update(data)

    def delete(self, user_id) -> None:
        self.user_dao.delete(user_id)
