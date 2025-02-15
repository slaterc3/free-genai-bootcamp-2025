from flask import jsonify, request
from . import api
from ..services.study_service import StudyService
from ..schemas.study_activity import StudyActivitySchema
from ..schemas.study_session import StudySessionSchema

study_service = StudyService()
activity_schema = StudyActivitySchema()
session_schema = StudySessionSchema()
sessions_schema = StudySessionSchema(many=True)

@api.route('/study-activities/<int:id>', methods=['GET'])
def get_study_activity(id):
    """Get study activity details"""
    activity = study_service.get_activity_by_id(id)
    return jsonify(activity_schema.dump(activity))

@api.route('/study-activities/<int:id>/sessions', methods=['GET'])
def get_activity_sessions(id):
    """Get all study sessions for an activity"""
    sessions = study_service.get_sessions_by_activity(id)
    return jsonify({
        'sessions': sessions_schema.dump(sessions)
    })

@api.route('/study-activities/<int:id>/sessions/<int:session_id>/launch', methods=['POST'])
def launch_session(id, session_id):
    """Launch a study session"""
    session = study_service.launch_session(id, session_id)
    return jsonify({
        'session_id': session.id,
        'group_id': session.group_id,
        'study_activity_id': session.study_activity_id,
        'redirect_url': f"{session.study_activity.url}/session/{session.id}"
    }) 