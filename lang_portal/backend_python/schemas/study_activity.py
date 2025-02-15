from .. import ma
from ..models.study_activity import StudyActivity

class StudyActivitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = StudyActivity
        
    id = ma.auto_field()
    name = ma.auto_field()
    url = ma.auto_field()
    created_at = ma.auto_field() 