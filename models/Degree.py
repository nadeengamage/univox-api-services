"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Degrees.
"""

from app import app, db
from models.Faculty import Faculty

class Degree(db.Model):
    __tablename__ = 'tbl_degrees'

    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column('deg_faculty_id',db.Integer, db.ForeignKey('tbl_faculties.id'), nullable=False)
    faculty = db.relationship('Faculty', backref='tbl_degrees', uselist=False)
    degree_code = db.Column('deg_degree_code',db.String(10), unique=True, nullable=False)
    degree_name = db.Column('deg_degree_name',db.String(60), unique=True, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
