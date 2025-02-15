from flask import Blueprint

api = Blueprint('api', __name__)

# Import routes after creating blueprint to avoid circular imports
from .words import *
from .groups import *
from .study_activities import *
from .study_sessions import *
from .settings import *
from .dashboard import * 