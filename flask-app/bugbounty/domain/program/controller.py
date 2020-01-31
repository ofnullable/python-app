from flask import Blueprint
from flask_apispec import marshal_with, use_kwargs
from sqlalchemy import text

from .models import Program, ProgramPolicy
from .serializer import program_response, programs_response, register_program_policy
from ..user.models import User
from ...env.exceptions import Commons

bp = Blueprint('programs', __name__, url_prefix='/api/v1')


@bp.route('/program', methods=('POST',))
@use_kwargs(register_program_policy, locations=['json'])
@marshal_with(program_response)
def register_program(**kwargs):
    writer = User.get_by_id(record_id=kwargs.get('writer_id'))
    program = Program.get_by_id(record_id=kwargs.get('program_id'))

    if not writer or not program:
        raise Commons.resource_not_found("Can not find vendor or program..")

    ProgramPolicy(writer=writer, program=program, **kwargs).save()
    return program


@bp.route('/program/<int:program_id>', methods=('PATCH',))
@use_kwargs(register_program_policy, locations=['json'])
@marshal_with(program_response)
def update_program(program_id):
    pass


@bp.route('/programs', methods=('GET',))
@marshal_with(programs_response)
def get_programs():
    return Program.query.order_by(Program.id.desc())
