from application.dao.model.user import User


class UserDAO:
    """
    DAO User
    """
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User).all()

    def get_by_user_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id).first()

    def create_user(self, data) -> bool:
        try:
            new_user = self.session.add(User(**data))
            self.session.commit()
            return new_user
        except Exception as e:
            print(f"Error adding user:\n{e}")
            self.session.rollback()
            return False

    def update_user(self, data: dict):
        try:
            user = self.get_by_user_id(data.get("id"))
            if data.get("name"):
                user.name = data.get("name")
            if data.get("role"):
                user.role = data.get("role")
            if data.get("password"):
                user.password = data.get("password")
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            print(f"Error update movie:\n{e}")
            self.session.rollback()

        # def update_user(self, data: dict):
        #     try:
        #         self.session.query(User).filter(User.id == data.get("id")).update(data)
        #         self.session.commit()
        #     except Exception as e:
        #         print(f"Error update user:\n{e}")
        #         self.session.rollback()

    def delete(self, user_id):
        try:
            self.session.query(User).filter(User.id == user_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete movie:\n{e}")
            self.session.rollback()

