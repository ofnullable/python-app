from flask import Blueprint

from .models import User
from bugbounty.env.database import db

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/users', methods=('POST',))
def register_user(username, email, password, **kwargs):
    try:
        user = User(username=username, email=email, password=password, **kwargs).save()
        return user.to_json()
    except Exception:
        db.session.rollback()
        raise KeyError('error occurred')
