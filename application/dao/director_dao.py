from application.dao.model.director import Director


class DirectorDAO:
    """
    DAO Director
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_id(self, director_id):
        return self.session.query(Director).filter(Director.id == director_id).first()

    def create_director(self, data) -> bool:
        try:
            new_director = self.session.add(Director(**data))
            self.session.commit()
            return new_director
        except Exception as e:
            print(f"Error adding director:\n{e}")
            self.session.rollback()
            return False

    def update_director(self, data: dict):
        try:
            self.session.query(Director).filter(Director.id == data.get("id")).update(data)
            self.session.commit()
        except Exception as e:
            print(f"Error update director:\n{e}")
            self.session.rollback()
            return False

    def delete(self, director_id):
        try:
            self.session.query(Director).filter(Director.id == director_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete director:\n{e}")
            self.session.rollback()
            return False
