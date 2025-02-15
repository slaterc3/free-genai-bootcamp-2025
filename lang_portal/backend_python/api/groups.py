from flask import jsonify, request
from . import api
from ..services.group_service import GroupService
from ..schemas.group import GroupSchema

group_service = GroupService()
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

@api.route('/groups', methods=['GET'])
def get_groups():
    """Get all groups"""
    groups = group_service.get_all()
    return jsonify(groups_schema.dump(groups))

@api.route('/groups/<int:id>', methods=['GET'])
def get_group(id):
    """Get a specific group's details"""
    group = group_service.get_by_id(id)
    return jsonify(group_schema.dump(group)) 