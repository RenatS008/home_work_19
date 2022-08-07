from marshmallow import Schema, fields
from setup_db import db


class Genre(db.Model):
    """
    Model for Genre
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
    Schema for Genre
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
