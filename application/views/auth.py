from flask import request
from flask_restx import Resource, Namespace

from application.service.auth import generate_token_for_user, check_token
from implemented import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        """
        Добавление нового Пользователя
        """
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return "Нет пароля или логина", 400

        user = user_service.get_by_username(username=username)
        return generate_token_for_user(username=username,
                                       password=password,
                                       password_hash=user.password,
                                       is_refresh=False), 201

    def put(self):
        """
        Изменить информацию о Пользователь по его id
        """
        data = request.json
        if not data.get("refresh_token"):
            return "", 400

        return check_token(data.get("refresh_token")), 200

