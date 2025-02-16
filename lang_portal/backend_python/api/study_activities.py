from flask import jsonify, request
from . import api
from ..models.study_activity import StudyActivity
from ..schemas.study_activity import study_activity_schema, study_activities_schema
from ..services.study_service import StudyService
from ..schemas.study_session import StudySessionSchema

study_service = StudyService()
sessions_schema = StudySessionSchema(many=True)

@api.route('/study-activities', methods=['GET'])
def get_study_activities():
    activities = StudyActivity.query.all()
    return jsonify(study_activities_schema.dump(activities))

@api.route('/study-activities/<int:id>', methods=['GET'])
def get_study_activity(id):
    activity = StudyActivity.query.get_or_404(id)
    return jsonify(study_activity_schema.dump(activity))

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