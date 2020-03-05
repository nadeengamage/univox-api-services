"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Faculties.
"""

from app import app, db
from models import Degree

class Faculty(db.Model):
    __tablename__ = 'tbl_faculties'

    id = db.Column(db.Integer, primary_key=True)
    faculty_code = db.Column('fac_code',db.String(10), unique=True, nullable=False)
    faculty_name = db.Column('fac_name',db.String(50), unique=True, nullable=False)
    degree = db.relationship('Degree', backref='tbl_degrees', uselist=False)
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
