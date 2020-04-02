"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Student Marks Schema.
"""

from app import ma
from models import Permission
from schemas.RoleSchema import RoleSchema

class PermissionSchema(ma.Schema):

    # Relation
    role = ma.Nested(RoleSchema)

    class Meta:
        model = Permission
        fields = ('role_code', 'controller', 'read', 'write', 'add', 'delete', 'status')