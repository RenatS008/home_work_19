from application.dao.model.genre import Genre


class GenreDAO:
    """
    DAO Genre
    """

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_id(self, genre_id):
        try:
            return self.session.query(Genre).filter(Genre.id == genre_id).one()
        except Exception as e:
            print(f"Error: genre with id:{genre_id}, not found.\n{e}")


    def create(self, **kwargs):
        try:
            new_id = self.session.add(Genre(**kwargs))
            self.session.commit()
            return new_id
        except Exception as e:
            print(f"Error adding genre:\n{e}")
            self.session.rollback()
            return False

    def update(self, data: dict) -> None:

        try:
            genre_id = self.session.query(Genre).filter(Genre.id == data.get("id")).update(data)
            self.session.commit()
            return genre_id
        except Exception as e:
            print(f"Error update genre:\n{e}")
            self.session.rollback()

    def delete(self, genre_id) -> None:
        try:
            self.session.query(Genre).filter(Genre.id == genre_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete movie:\n{e}")
            self.session.rollback()
