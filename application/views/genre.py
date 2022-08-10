from flask import request
from flask_restx import Resource, Namespace

from application.dao.model.genre import GenreSchema
from application.service.protection import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    @auth_required
    def get(self):
        """
        Получение списка всех жанров
        """
        return genre_schema.dump(genre_service.get_all()), 200

    @admin_required
    def post(self):
        """
        Добавление нового Режиссера
        """
        data = request.json
        if genre_service.create(data):
            new_genre = genre_service.create(data)
            if new_genre:
                return "Режиссер успешно добавлен.", \
                       {'location': f'/directors/{new_genre}'}, 201

        else:
            return "Режиссер не добавлен.", 503
        data = request.json
        if genre_id := genre_service.create(data):
            return "Жанр успешно добавлен.", 201, \
                   {'location': f'/genres/{genre_id}'}
        else:
            return "Жанр не добавлен.", 503


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    @auth_required
    def get(self, genre_id: int):
        """
        Получение жанра по его id
        """
        return genre_schema.dump([(genre_service.get_by_id(genre_id))]), 200

    @admin_required
    def put(self, genre_id: int):
        """
        Изменить информацию о жанре по его id
        """
        data = request.json
        if not data.get('id') or (data.get('id') != genre_id):
            data['id'] = genre_id
        if genre_schema.dump(genre_service.update(data)):
            genre_id = genre_service.update(data)
            return "Успешно удалось изменить информацию о Жанре.", \
                   {'location': f'/directors/{genre_id}'}, 201
        else:
            return "Изменить информацию о жанре не удалось.", 502

    @admin_required
    def delete(self, genre_id: int):
        """
        Удаление Жанра по его id
        """
        if genre_schema.dump(genre_service.delete(genre_id)):
            data = genre_schema.dump(genre_service.delete(genre_id))
            return "Жанр успешно удален.", data, 204
        else:
            return "Жанр не удален.", 502
