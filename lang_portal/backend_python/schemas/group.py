from .. import ma
from ..models.group import Group

class GroupSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Group
        
    id = ma.auto_field()
    name = ma.auto_field()
    words_count = ma.auto_field()
    created_at = ma.auto_field()
    words = ma.Nested('WordSchema', many=True, exclude=('groups',))

# Create schema instances
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True) 