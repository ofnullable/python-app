from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with

from .models import User
from .serializer import register_hacker, hacker_response, register_vendor, \
    vendor_response
from ..program.models import Program

bp = Blueprint('user', __name__)


@bp.route('/api/user', methods=('POST',))
@use_kwargs(register_hacker, locations=['json'])
@marshal_with(hacker_response)
def register_user(**kwargs):
    try:
        user = User(is_vendor=False, **kwargs).save()
        return user
    except Exception:
        raise Exception('Fail to register user')


@bp.route('/api/user/<username>', methods=('GET',))
@marshal_with(hacker_response)
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return user
    else:
        raise Exception('User not found')


@bp.route('/api/vendor', methods=('POST',))
@use_kwargs(register_vendor, locations=['json'])
@marshal_with(vendor_response)
def register_vendor(**kwargs):
    try:
        vendor = User(is_vendor=True, **kwargs).save()
        Program(vendor=vendor).save()

        return vendor
    except Exception:
        raise Exception('Fail to register user')
