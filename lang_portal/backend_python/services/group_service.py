from .. import db
from ..models.group import Group

class GroupService:
    def get_all(self):
        return Group.query.all()
    
    def get_by_id(self, id):
        return Group.query.get_or_404(id) 