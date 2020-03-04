"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application users.
"""

from app import app, db

class Degree(db.Model):
    __tablename__ = 'degrees'

    id = db.Column(db.Integer, primary_key=True)
    faculty = db.Column(db.Integer)
    degree_code = db.Column(db.String(10), unique=True)
    degree_name = db.Column(db.String(60), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, degree_code):
        self.degree_code
        pass
