from .. import db
from ..models.study_activity import StudyActivity
from ..models.study_session import StudySession

class StudyService:
    def get_activity_by_id(self, id):
        return StudyActivity.query.get_or_404(id)
    
    def get_sessions_by_activity(self, activity_id):
        return StudySession.query.filter_by(study_activity_id=activity_id).all()
    
    def get_last_session(self):
        return StudySession.query.order_by(StudySession.created_at.desc()).first()
    
    def get_progress_stats(self):
        # Implement progress calculation logic
        return {} 