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
        return self.session.query(Genre).filter(Genre.id == genre_id).one()

    def create_genre(self, data) -> bool:
        try:
            new_genre = self.session.add(Genre(**data))
            self.session.commit()
            return new_genre
        except Exception as e:
            print(f"Error adding genre:\n{e}")
            self.session.rollback()
            return False

    def update_genre(self, data: dict):
        try:
            self.session.query(Genre).filter(Genre.id == data.get("id")).update(data)
            self.session.commit()
        except Exception as e:
            print(f"Error update genre:\n{e}")
            self.session.rollback()

    def delete(self, genre_id):
        try:
            self.session.query(Genre).filter(Genre.id == genre_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete movie:\n{e}")
            self.session.rollback()
