"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Role Permission Model.
"""

from app import app, db
from models import Role

class Permission(db.Model):
    __tablename__ = 'tbl_permissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    read = db.Column(db.Boolean, nullable=False)
    write = db.Column(db.Boolean, nullable=False)
    add = db.Column(db.Boolean, nullable=False)
    delete = db.Column(db.Boolean, nullable=False)
    role_code = db.Column('role_permission_role_code', db.String(10), db.ForeignKey('tbl_roles.id'), nullable=False)
    controller = db.Column('role_permission_controller', db.String(80))
    status = db.Column(db.Boolean, nullable=False)
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


