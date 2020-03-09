"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import app, db

class Diploma(db.Model):
    __tablename__ = 'tbl_diplomas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dip_code = db.Column('dip_diploma_code',db.String(10), unique=True, nullable=False)
    dip_name = db.Column('dip_diploma_name',db.String(60), unique=True, nullable=False)
    duration = db.Column(db.String(50))
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
