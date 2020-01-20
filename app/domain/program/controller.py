from flask import Blueprint, request

bp = Blueprint('program_bp', __name__)


@bp.route('/', methods=['POST'])
def post():
    if request.method != 'POST':
        pass

    body = request.get_json(silent=True)

    print(body)
