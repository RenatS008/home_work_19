from application.dao.movie_dao import MovieDAO
from application.dao.model.movie import Movie


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self) -> list[Movie]:
        return self.movie_dao.get_all()

    def get_by(self, **kwargs):
        return self.movie_dao.gets_universal(**kwargs)

    def create(self, data) -> None:
        return self.movie_dao.create(**data)

    def update(self, data) -> None:
        return self.movie_dao.update(data)

    def delete(self, movie_id) -> None:
        self.movie_dao.delete(movie_id)
