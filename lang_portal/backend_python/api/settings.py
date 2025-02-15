from flask import jsonify
from . import api

@api.route('/settings', methods=['GET'])
def get_settings():
    """Get application settings"""
    return jsonify({
        'version': '0.1.0',
        'environment': 'development'
    }) 