from flask import jsonify, request
from . import api
from ..models.group import Group
from ..schemas.group import group_schema, groups_schema

@api.route('/groups', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    return jsonify(groups_schema.dump(groups))

@api.route('/groups/<int:id>', methods=['GET'])
def get_group(id):
    group = Group.query.get_or_404(id)
    return jsonify(group_schema.dump(group)) 