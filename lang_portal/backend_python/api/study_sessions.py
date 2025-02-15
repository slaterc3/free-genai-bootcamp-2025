from flask import jsonify
from . import api
from ..services.study_service import StudyService
from ..schemas.study_session import StudySessionSchema

study_service = StudyService()
session_schema = StudySessionSchema()

@api.route('/study-sessions/<int:id>', methods=['GET'])
def get_study_session(id):
    """Get study session details"""
    session = study_service.get_session_by_id(id)
    return jsonify(session_schema.dump(session)) 