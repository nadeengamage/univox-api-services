"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application users.
"""

from app import app, db

class Degree(db.Model):
    __tablename__ = 'tbl_degrees'

    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer)
    degree_code = db.Column(db.String(10), unique=True)
    degree_name = db.Column(db.String(60), unique=True)
    status = db.Column(db.Boolean)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
