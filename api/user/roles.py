"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - User role controller.
"""

from app import app
from flask import jsonify 
from models.Role import Role
from schemas.RoleSchema import RoleSchema
from flask_jwt import JWT, jwt_required, current_identity

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

# get all roles
@app.route('/roles')
# @jwt_required()
def get_roles():
    users = Role.query.all()
    return {'data': roles_schema.dump(users)}, 200