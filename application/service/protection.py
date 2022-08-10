import jwt
from flask import request, abort
from config import Config
from implemented import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        if not token:
            return "The token is missing"

        try:
            jwt.decode(token, key=Config['SECRET_KEY'],
                       algorithms=Config['ALGORITHMS'])
            return func(*args, **kwargs)
        except Exception:
            raise Exception

    return wrapper

    # def wrapper(*args, **kwargs):
    #     if "Authorization" not in request.headers:
    #         abort(401)
    #     data = request.headers['Authorization']
    #     token = data.split("Bearer ")[-1]
    #     try:
    #         jwt.decode(token, secret=Config['SECRET_KEY'],
    #                    algorithms=Config['ALGORITHMS'])
    #     except Exception as e:
    #         print(f"Traceback: {e}")
    #         abort(401)
    #     return func(*args, **kwargs)
    # return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        if not token:
            return "The token is missing"

        try:
            data = jwt.decode(token, key=Config['SECRET_KEY'],
                              algorithms=Config['ALGORITHMS'])
            if user_service.get_by_username(data['username']).role == "admin":
                return func(*args, **kwargs)
            else:
                return "You don't have access rights"
        except Exception:
            raise Exception

    return wrapper
    # def wrapper(*args, **kwargs):
    #     if "Authorization" not in request.headers:
    #         abort(401)
    #     data = request.headers['Authorization']
    #     token = data.split("Bearer ")[-1]
    #     try:
    #         user = jwt.decode(token, secret=Config['SECRET_KEY'],
    #                           algorithms=Config['ALGORITHMS'])
    #         role = user.get("role")
    #     except Exception as e:
    #         print("JWT Decode Exception", e)
    #         abort(401)
    #     if role != "admin":
    #         abort(403)
    #     return func(*args, **kwargs)
    #
    # return wrapper()

# def auth_required(func):
#     def wrapper(*args, **kwargs):
#         # if request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', ''):
#         token = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
#         if not token:
#             raise Exception
#         try:
#             jwt.decode(token, secret=Config['SECRET_KEY'],
#                        algorithm=Config['ALGORITHM'])
#             return func(*args, **kwargs)
#         except Exception:
#             raise Exception
#
#     return wrapper()
#
#
# def admin_required(func):
#     def wrapper(*args, **kwargs):
#         # if request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', ''):
#
#         token = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
#         if not token:
#             raise Exception
#         try:
#             data = jwt.decode(token, secret=Config['SECRET_KEY'],
#                               algorithms=Config['ALGORITHM'])
#
#             if data['role'] == "admin":
#                 return func(*args, **kwargs)
#             else:
#                 Exception
#         except Exception as e:
#             print("JWT Decode Exception", e)
#             abort(401)
#
#     return wrapper()
