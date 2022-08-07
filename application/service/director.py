from application.dao.director_dao import DirectorDAO
from application.dao.model.director import Director


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_by_id(self, director_id):
        return self.director_dao.get_by_id(director_id)

    def get_all(self) -> list[Director]:
        return self.director_dao.get_all()

    def add_director(self, data):
        self.director_dao.create_director(**data)

    def update(self, data):
        self.director_dao.update_director(data)

    def delete(self, director_id):
        self.director_dao.delete(director_id)
