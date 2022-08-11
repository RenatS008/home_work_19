from flask import request
from flask_restx import Resource, Namespace

from application.dao.model.director import DirectorSchema
from application.service.protection import admin_required, auth_required

from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    @auth_required
    def get(self):
        """
        Получение списка всех режиссёров
        """
        return director_schema.dump(director_service.get_all()), 200

    @admin_required
    def post(self):
        """
        Добавление нового Режиссера
        """
        data = request.json
        if director_service.create(data):
            new_director = director_service.create(data)
            if new_director:
                return "Режиссер успешно добавлен.", \
                       {'location': f'/directors/{new_director}'}, 201

        else:
            return "Режиссер не добавлен.", 503


@director_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    @auth_required
    def get(self, director_id: int):
        """
        Получение режиссера по его id
        """
        if director_schema.dump([director_service.get_by_id(director_id)]):
            return director_schema.dump([director_service.get_by_id(director_id)]), 200
        else:
            return print(f"Error: director with id:{director_id}, not found."), 502

    @admin_required
    def put(self, director_id: int):
        """
        Изменить информацию о Режиссере по его id
        """
        data = request.json
        if not data.get('id') or (data.get('id') != director_id):
            data['id'] = director_id
        if director_schema.dump(director_service.update(data)):
            director_id = director_service.update(data)
            return "Успешно удалось изменить информацию о Режиссере.", \
                   {'location': f'/directors/{director_id}'}, 201
        else:
            return "Изменить информацию о фильме не удалось.", 502

    @admin_required
    def delete(self, director_id: int):
        """
        Удаление Режиссера по его id
        """
        if director_schema.dump(director_service.delete(director_id)):
            data = director_schema.dump(director_service.delete(director_id))
            return "Режиссер успешно удален.", data, 204
        else:
            return "Режиссер не удален.", 502
