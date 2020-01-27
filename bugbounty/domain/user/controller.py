from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with

from bugbounty.env.database import db
from .models import User
from .serializer import register_user, user_response

bp = Blueprint('user', __name__)


@bp.route('/api/users', methods=['POST'])
@use_kwargs(register_user, locations=['json'])
@marshal_with(user_response)
def register_user(**kwargs):
    print(kwargs)
    try:
        user = User(**kwargs).save()
        return user
    except Exception:
        db.session.rollback()
        raise KeyError('error occurred')
