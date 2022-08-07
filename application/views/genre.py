from flask import request
from flask_restx import Resource, Namespace

from application.dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        """
        Получение списка всех жанров
        """
        return genre_schema.dump(genre_service.get_all()), 200

    def post(self):
        """
        Добавление нового Режиссера
        """
        data = request.json
        if genre_service.add_genre(data):
            new_genre = genre_service.add_genre(data)
            if new_genre:
                return "Жанр успешно добавлен.", 201, \
                       {'location': f'/genres/{new_genre}'}

        else:
            return "Жанр не добавлен.", 503


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    def get(self, genre_id: int):
        """
        Получение жанра по его id
        """
        return genre_schema.dump([(genre_service.get_by_id(genre_id))]), 200

    def put(self, genre_id: int):
        """
        Изменить информацию о жанрае по его id
        """
        data = request.json
        if genre_schema.dump(genre_service.update(data)):
            upd_genre = genre_schema.dump(genre_service.update(data))
            return "Успешно удалось изменить информацию о Жанре.", \
                   201, {'location': f'/genres/{upd_genre}'}
        else:
            return "Изменить информацию о Жанре не удалось.", 502

    def delete(self, genre_id: int):
        """
        Удаление жанра по его id
        """
        if genre_schema.dump(genre_service.delete(genre_id)):
            return "Жанр успешно удален.", 204
        else:
            return "Жанр не удален.", 502
