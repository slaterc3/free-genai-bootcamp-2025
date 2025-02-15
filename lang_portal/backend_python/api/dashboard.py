from flask import jsonify
from . import api
from ..services.study_service import StudyService
from ..schemas.study_session import StudySessionSchema

study_service = StudyService()
session_schema = StudySessionSchema()

@api.route('/dashboard/last-session', methods=['GET'])
def get_last_session():
    """Get the user's last study session"""
    session = study_service.get_last_session()
    if not session:
        return jsonify({'session': None})
    return jsonify(session_schema.dump(session))

@api.route('/dashboard/stats', methods=['GET'])
def get_stats():
    """Get study statistics"""
    stats = study_service.get_progress_stats()
    return jsonify(stats) 