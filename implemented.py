from application.dao.director_dao import DirectorDAO
from application.dao.genre_dao import GenreDAO
from application.dao.movie_dao import MovieDAO
from application.dao.user_dao import UserDAO
from application.service.director import DirectorService
from application.service.genre import GenreService
from application.service.movie import MovieService
from application.service.user import UserService
from setup_db import db


movie_service = MovieService(movie_dao=MovieDAO(db.session))

genre_service = GenreService(genre_dao=GenreDAO(db.session))

director_service = DirectorService(director_dao=DirectorDAO(db.session))

user_service = UserService(user_dao=UserDAO(db.session))
