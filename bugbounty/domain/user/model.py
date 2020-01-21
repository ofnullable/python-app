from _datetime import datetime

from bugbounty import db
from bugbounty.env.base_model import BaseModel


class User(BaseModel, db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(150), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, unique=False, nullable=False)
    created = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email, password=None, is_admin=False):
        # db.Model.__init__(self, username=username, email=email, password=password, is_admin=is_admin)
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
