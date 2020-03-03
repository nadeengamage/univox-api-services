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

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

# get all roles
@app.route('/roles')
def get_roles():
    users = Role.query.all()
    return {'data': roles_schema.dump(users)}, 200