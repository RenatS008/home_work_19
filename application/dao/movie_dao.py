from application.dao.model.movie import Movie


class MovieDAO:
    """
    DAO Movie
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, movie_id):
        return self.session.query(Movie).filter(Movie.id == movie_id).first()

    def get_all_movie_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_all_movie_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def gets_universal(self, **kwargs):
        """
        Universal function for search
        """
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create_movie(self, data) -> bool:
        try:
            new_movie = self.session.add(Movie(**data))
            self.session.commit()
            return new_movie
        except Exception as e:
            print(f"Error adding movie:\n{e}")
            self.session.rollback()
            return False

    def update_movie(self, data: dict):
        try:
            self.session.query(Movie).filter(Movie.id == data.get("id")).update(data)
            self.session.commit()
        except Exception as e:
            print(f"Error update movie:\n{e}")
            self.session.rollback()

    def delete(self, movie_id):
        try:
            self.session.query(Movie).filter(Movie.id == movie_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete movie:\n{e}")
            self.session.rollback()
