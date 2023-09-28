from flask_sqlalchemy import *
from uuid import uuid4

db = SQLAlchemy()


def get_uid():
    return uuid4().hex


class User(db.Model):
    __tableName__ = "users"
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uid)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.Text, nullable=False)

