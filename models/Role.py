"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application user roles.
"""

from app import app, db
from models.User import User
from models.Permission import Permission


class Role(db.Model):
    __tablename__ = 'tbl_roles'

    id = db.Column(db.Integer, primary_key=True)
    role_code = db.Column(db.String(10), unique=True)
    role_name = db.Column(db.String(50), unique=True)
    users = db.relationship('User', backref='tbl_roles', uselist=False)
    permission = db.relationship('Permission', backref='tbl_roles', uselist=True)
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
