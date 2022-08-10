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
        return self.session.query(Director).filter(Director.id == director_id).one()

    def create(self, **kwargs):
        try:
            new_id = self.session.add(Director(**kwargs))
            self.session.commit()
            return new_id
        except Exception as e:
            print(f"Error adding director:\n{e}")
            self.session.rollback()
            return False

    def update(self, data: dict) -> None:
        try:
            director_id = self.session.query(Director).filter(Director.id == data.get("id")).update(data)
            self.session.commit()
            return director_id
        except Exception as e:
            print(f"Error update director:\n{e}")
            self.session.rollback()

    def delete(self, director_id) -> None:
        try:
            self.session.query(Director).filter(Director.id == director_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete director:\n{e}")
            self.session.rollback()

