import json

from bugbounty.env.extensions import db
from bugbounty.env.util import AlchemyEncoder


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

    def to_json(self, show=None):
        return json.dumps(self, cls=AlchemyEncoder)
