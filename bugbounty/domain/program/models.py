import datetime as dt

from bugbounty.env.database import db, BaseModel, Column, Model


class Program(BaseModel, Model):
    __tablename__ = 'programs'

    title = Column(db.String(64), unique=True, nullable=False)
    contents = Column(db.Text, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, title, contents):
        # db.Model.__init__(self, username=username, email=email, password=password, is_admin=is_admin)
        self.title = title
        self.contents = contents
