from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with

from .models import Program
from .serializer import programs_response

bp = Blueprint('programs', __name__)


@bp.route('/api/programs', methods=('GET',))
@marshal_with(programs_response)
def get_programs():
    return Program.query.all()
