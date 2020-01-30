from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .extensions import db

Model = db.Model
Column = db.Column
relationship = relationship


class BaseModel:
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, record_id):
        """Get record by ID."""
        if any(
                (isinstance(record_id, (str, bytes)) and record_id.isdigit(),
                 isinstance(record_id, (int, float))),
        ):
            return cls.query.get(int(record_id))


class BaseTimeModel(BaseModel):
    __table_args__ = {'extend_existing': True}

    created_at = Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


def reference_col(tablename, nullable=False, pk_name='id', **kwargs):
    """Column that adds primary key foreign key reference.

    Usage: ::
        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    return db.Column(
        db.ForeignKey(
            '{0}.{1}'.format(tablename, pk_name)), nullable=nullable, **kwargs)
