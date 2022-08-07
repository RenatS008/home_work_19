from marshmallow import Schema, fields

from application.dao.model.director import Director
from application.dao.model.genre import Genre
from setup_db import db


class Movie(db.Model):
    """
    Model for Movie
    """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey(f"{Genre.__tablename__}.id"))
    director_id = db.Column(db.Integer, db.ForeignKey(f"{Director.__tablename__}.id"))

    genre = db.relationship("Genre")
    director = db.relationship("Director")


class MovieSchema(Schema):
    """
    Schema for Movie
    """
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre_id = fields.Int()
    genre = fields.Str()
    director_id = fields.Int()
    director = fields.Str()
