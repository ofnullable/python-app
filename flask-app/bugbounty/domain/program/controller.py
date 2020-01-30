from flask import Blueprint
from flask_apispec import marshal_with, use_kwargs

from .models import Program, ProgramPolicy
from .serializer import program_response, programs_response, register_program_policy
from ..user.models import User

bp = Blueprint('programs', __name__)


@bp.route('/api/program', methods=('POST',))
@use_kwargs(register_program_policy, locations=['json'])
@marshal_with(program_response)
def register_program(**kwargs):
    writer = User.get_by_id(record_id=kwargs.get('writer_id'))
    program = Program.get_by_id(record_id=kwargs.get('program_id'))

    if not writer or not program:
        print(writer, program)
        raise Exception('Can not find writer or program..')

    ProgramPolicy(writer=writer, program=program, **kwargs).save()
    return program


@bp.route('/api/programs', methods=('GET',))
@marshal_with(programs_response)
def get_programs():
    return Program.query.all()
