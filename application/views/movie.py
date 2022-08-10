from flask import request
from flask_restx import Resource, Namespace

from application.dao.model.movie import MovieSchema
from application.service.protection import auth_required, admin_required

from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
@movie_ns.param("director_id", description="получить все фильмы режиссера")
@movie_ns.param("genre_id", description="получить все фильмы жанра")
@movie_ns.param("year", description="получить все фильмы за год")
class MovieView(Resource):

    def get(self):
        """
        Поиск фильмов по нескольким параметрам, если параметр не задан,
        выдаем весь список.
        """
        if len(request.args) > 0:
            return movie_schema.dump(movie_service.get_by(**request.args))
        else:
            return movie_schema.dump(movie_service.get_all()), 200

    @admin_required
    def post(self):
        """
        Добавление нового фильма
        """
        if movie_service.create(request.json):
            movie_id = movie_service.create(request.json)
            return "Фильм успешно добавлен.", \
                   {'location': f'/movies/{movie_id}'}, 201
        else:
            return "Фильм не добавлен.", 503


@movie_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    @auth_required
    def get(self, movie_id: int):
        """
        Получение фильмов по его id
        """
        return movie_schema.dump(movie_service.get_by(movie_id)), 200

    @admin_required
    def put(self, movie_id: int):
        """
        Изменить информацию о фильме по его id
        """
        if movie_schema.dump(movie_service.update(request.json)):
            movie_id = movie_service.update(request.json)
            return "Успешно удалось изменить информацию о фильме.", \
                   {'location': f'/movies/{movie_id}'}, 201
        else:
            return "Изменить информацию о фильме не удалось.", 502

    @admin_required
    def delete(self, movie_id: int):
        """
        Удаление фильма по его id
        """
        if movie_schema.dump(movie_service.delete(movie_id)):
            return "Фильм успешно удален.", 204
        else:
            return "Фильм не удален.", 502

