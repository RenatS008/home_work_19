from flask import request
from flask_restx import Resource, Namespace

from application.dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        """
        Получение списка всех режиссёров
        """
        return director_schema.dump(director_service.get_all()), 200

    def post(self):
        """
        Добавление нового Режиссера
        """
        data = request.json
        if director_service.add_director(data):
            new_director = director_service.add_director(data)
            if new_director:
                return "Режиссер успешно добавлен.", 201, \
                       {'location': f'/directors/{new_director}'}

        else:
            return "Режиссер не добавлен.", 503


@director_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    def get(self, director_id: int):
        """
        Получение режиссера по его id
        """
        return director_schema.dump([director_service.get_by_id(director_id)]), 200

    def put(self, director_id: int):
        """
        Изменить информацию о Режиссере по его id
        """
        data = request.json
        if director_schema.dump(director_service.update(data)):
            upd_director = director_service.update(data)
            return "Успешно удалось изменить информацию о Режиссере.", \
                   201, {'location': f'/directors/{upd_director}'}
        else:
            return "Изменить информацию о фильме не удалось.", 502

    def delete(self, director_id: int):
        """
        Удаление Режиссера по его id
        """
        if director_schema.dump(director_service.delete(director_id)):
            return "Режиссер успешно удален.", 204
        else:
            return "Режиссер не удален.", 502

