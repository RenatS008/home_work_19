from application.dao.model.user import User


class UserDAO:
    """
    DAO User
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id).one()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def create(self, data):
        try:
            user = User(**data)
            self.session.add(user)
            self.session.commit()
            return user
        except Exception as e:
            print(f"Error adding user:\n{e}")
            self.session.rollback()
            return False

    # def update(self, data: dict) -> None:
    #     try:
    #         user = self.get_by_id(data.get("id"))
    #         if data.get("name"):
    #             user.name = data.get("name")
    #         if data.get("role"):
    #             user.role = data.get("role")
    #         if data.get("password"):
    #             user.password = data.get("password")
    #         self.session.add(user)
    #         self.session.commit()
    #         return user
    #     except Exception as e:
    #         print(f"Error update movie:\n{e}")
    #         self.session.rollback()

    def update(self, data: dict) -> None:
        # try:
        #     user_id = self.session.query(User).filter(User.id == data.get("id")).update(data)
        #     self.session.commit()
        #     return user_id
        # except Exception as e:
        #     print(f"Error update user:\n{e}")
        #     self.session.rollback()

        try:
            user = self.get_by_id(data.get("id"))
            if data.get("name"):
                user.name = data.get("name")
            if data.get("role"):
                user.name = data.get("role")
            if data.get("password"):
                user.name = data.get("password")
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            print(f"Error update user:\n{e}")
            self.session.rollback()

    def delete(self, user_id):
        try:
            self.session.query(User).filter(User.id == user_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete user:\n{e}")
            self.session.rollback()
        # try:
        #     user = self.get_by_id(user_id)
        #     self.session.delete(user)
        #     self.session.commit()
        # except Exception as e:
        #     print(f"Error delete movie:\n{e}")
        #     self.session.rollback()



