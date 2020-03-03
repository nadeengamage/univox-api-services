"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application user roles.
"""

from app import app, db, ma

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_code = db.Column(db.String(10), unique=True)
    role_name = db.Column(db.String(50), unique=True)
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def __init__(self, role_code, role_name):
        self.role_code = role_code
        self.role_name = role_name
        pass

class RoleSchema(ma.Schema):
  class Meta:
    fields = ('id', 'role_code', 'role_name')