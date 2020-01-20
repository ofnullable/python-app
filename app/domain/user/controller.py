from flask import Blueprint, request, make_response, jsonify

from .model import db, User

bp = Blueprint('user_bp', __name__)


@bp.route('/', methods=['POST'])
def post():
    if request.method != 'POST':
        return make_response('Bad Request', 400)

    body = request.get_json(silent=True)

    print(body)

    return make_response(jsonify(body), 200)
