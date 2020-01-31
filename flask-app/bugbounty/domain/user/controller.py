from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from sqlalchemy.exc import IntegrityError

from .models import User
from .serializer import register_hacker, hacker_response, register_vendor, vendor_response
from ..program.models import Program
from ...env.exceptions import Commons

bp = Blueprint('users', __name__, url_prefix='/api/v1')


@bp.route('/user', methods=('POST',))
@use_kwargs(register_hacker, locations=['json'])
@marshal_with(hacker_response)
def register_user(**kwargs):
    try:
        user = User(is_vendor=False, **kwargs).save()
        return user, 201
    except IntegrityError:
        raise Commons.duplicate_key("username '{0}' is already exists".format(kwargs['username']))
    except Exception:
        raise Exception('Fail to register user')


@bp.route('/user/<string:username>', methods=('GET',))
@marshal_with(hacker_response)
def get_user(username):
    user = User.query.filter_by(username=username, is_vendor=False).scalar()
    if not user:
        raise Commons.resource_not_found("User not found for username: '{0}'".format(username))
    return user


@bp.route('/vendor', methods=('POST',))
@use_kwargs(register_vendor, locations=['json'])
@marshal_with(vendor_response)
def register_vendor(**kwargs):
    try:
        vendor = User(is_vendor=True, **kwargs).save(False)
        Program(vendor=vendor).save(True)

        return vendor, 201

    except IntegrityError:
        raise Commons.duplicate_key("vendor '{0}' is already exists".format(kwargs['username']))
    except Exception:
        raise Exception('Fail to register user')


@bp.route('/vendor/<string:vendor_name>', methods=('GET',))
@marshal_with(vendor_response)
def get_vendor(vendor_name):
    vendor = User.query.filter_by(username=vendor_name, is_vendor=True).scalar()
    if not vendor:
        raise Commons.resource_not_found("Vendor not found for vendor name: '{0}'".format(vendor_name))
    return vendor
