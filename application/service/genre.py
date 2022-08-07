from application.dao.genre_dao import GenreDAO
from application.dao.model.genre import Genre


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_by_id(self, genre_id):
        return self.genre_dao.get_by_id(genre_id)

    def get_all(self) -> list[Genre]:
        return self.genre_dao.get_all()

    def add_genre(self, data):
        self.genre_dao.create_genre(**data)

    def update(self, data):
        self.genre_dao.update_genre(data)

    def delete(self, genre_id):
        self.genre_dao.delete(genre_id)
