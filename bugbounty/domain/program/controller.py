from flask import Blueprint

from .models import Program
from bugbounty.env.database import db

bp = Blueprint('programs', __name__)


@bp.route('/api/programs', methods=['GET'])
def get_programs():
    return {'programs': Program.query.all()}
