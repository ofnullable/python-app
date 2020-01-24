from flask import Blueprint

from .models import Program
from bugbounty.env.database import db

bp = Blueprint('programs', __name__)

