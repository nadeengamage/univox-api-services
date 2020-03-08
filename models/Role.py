"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application user roles.
"""

from app import app, db

class Role(db.Model):
    __tablename__ = 'tbl_roles'

    id = db.Column(db.Integer, primary_key=True)
    role_code = db.Column(db.String(10), unique=True)
    role_name = db.Column(db.String(50), unique=True)
    users = db.relationship('User', backref='tbl_roles', uselist=False)
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
