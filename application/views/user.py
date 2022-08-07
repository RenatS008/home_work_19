from flask import request
from flask_restx import Resource, Namespace
from application.dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')
user_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        """
        Выдаем весь список пользователей.
        """
        return user_schema.dump(user_service.get_all()), 200

    def post(self):
        """
        Добавление нового Пользователя.
        """
        data = request.json
        if user_service.add_movie(data):
            new_user = user_service.add_movie(data)
            if new_user:
                return "Пользователь успешно добавлен.", 201, \
                       {'location': f'/users/{new_user}'}

        else:
            return "Пользователь не добавлен.", 503


@user_ns.route('/<int:user_id>/')
class UserView(Resource):
    def get(self, user_id: int):
        """
        Получение Пользователя по его id
        """
        return user_schema.dump(user_service.get_by(user_id)), 200

    def put(self, user_id: int):
        """
        Изменить информацию о Пользователе по его id
        """
        data = request.json
        if user_schema.dump(user_service.update(data)):
            upd_user = user_service.add_user(data)
            return "Успешно удалось изменить информацию о фильме.", 201, \
                   {'location': f'/users/{upd_user}'}
        else:
            return "Изменить информацию о Пользователе не удалось.", 502

    def delete(self, user_id: int):
        """
        Удаление Пользователя по его id
        """
        if user_schema.dump(user_service.delete(user_id)):
            return "Пользователь успешно удален.", 204
        else:
            return "Пользователь не удален.", 502
