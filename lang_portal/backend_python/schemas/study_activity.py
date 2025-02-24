from .. import ma
from ..models.study_activity import StudyActivity

class StudyActivitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = StudyActivity
        
    id = ma.auto_field()
    name = ma.auto_field()
    url = ma.auto_field()
    created_at = ma.auto_field() 

# Create schema instances
study_activity_schema = StudyActivitySchema()
study_activities_schema = StudyActivitySchema(many=True) 