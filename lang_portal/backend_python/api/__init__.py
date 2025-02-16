from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@api.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Import routes after creating blueprint to avoid circular imports
from . import study_activities, words, groups, dashboard
from .settings import *
from .study_sessions import * 