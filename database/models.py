from .db import db

class Items(db.Document):
    name = db.StringField(required=True, unique=True)
    price = db.StringField(required=True, unique=True)