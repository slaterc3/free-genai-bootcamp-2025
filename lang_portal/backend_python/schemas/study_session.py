from .. import ma
from ..models.study_session import StudySession

class StudySessionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = StudySession
        
    id = ma.auto_field()
    group_id = ma.auto_field()
    study_activity_id = ma.auto_field()
    created_at = ma.auto_field()
    correct_count = ma.Function(lambda obj: obj.correct_count)
    total_reviews = ma.Function(lambda obj: obj.total_reviews)
    
    # Nested relationships
    group = ma.Nested('GroupSchema', exclude=('study_sessions',))
    study_activity = ma.Nested('StudyActivitySchema', exclude=('study_sessions',)) 