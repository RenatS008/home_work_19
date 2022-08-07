from application.dao.movie_dao import MovieDAO
from application.dao.model.movie import Movie


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self) -> list[Movie]:
        return self.movie_dao.get_all()

    def get_by(self, id=None, director_id=None, genre_id=None, year=None):

        if director_id:
            return self.movie_dao.gets_universal(director_id=director_id)

        if genre_id:
            return self.movie_dao.gets_universal(genre_id=genre_id)

        if year:
            return self.movie_dao.gets_universal(year=year)

        if id:
            return self.movie_dao.gets_universal(id=id)

    def add_movie(self, data):
        self.movie_dao.create_movie(**data)

    def update(self, data):
        self.movie_dao.update_movie(data)

    def delete(self, movie_id):
        self.movie_dao.delete(movie_id)
