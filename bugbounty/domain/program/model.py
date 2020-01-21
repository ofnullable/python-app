from bugbounty import db
from bugbounty.env.base_model import BaseModel


class Program(BaseModel, db.Model):
    __tablename__ = 'programs'

    title = db.Column(db.String(64), unique=True, nullable=False)
    contents = db.Column(db.Text, nullable=False)

    def __init__(self, title, contents):
        # db.Model.__init__(self, username=username, email=email, password=password, is_admin=is_admin)
        self.title = title
        self.contents = contents
