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
        return self.session.query(Movie).filter(Movie.id == movie_id).one()

    def gets_universal(self, **kwargs):
        """
        Universal function for search
        """
        return self.session.query(Movie).filter_by(
            **{key: value for key, value in kwargs.items() if value is not None}
        ).all()

    def create(self, **kwargs):
        try:
            new_id = self.session.add(Movie(**kwargs))
            self.session.commit()
            return new_id
        except Exception as e:
            print(f"Error adding movie:\n{e}")
            self.session.rollback()
            return False

    def update(self, data: dict) -> None:
        try:
            movie_id = self.session.query(Movie).filter(Movie.id == data.get("id")).update(data)
            self.session.commit()
            return movie_id
        except Exception as e:
            print(f"Error update movie:\n{e}")
            self.session.rollback()

    def delete(self, movie_id) -> None:
        try:
            self.session.query(Movie).filter(Movie.id == movie_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error delete movie:\n{e}")
            self.session.rollback()
