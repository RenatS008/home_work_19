from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    """
    Model for Director
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
    Schema for Director
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
