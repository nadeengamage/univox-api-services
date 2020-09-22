"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - AL Student Report.
"""

from app import app, db

class ALReport(db.Model):
    __tablename__ = 'tbl_temp_al'

    id = db.Column(db.Integer, primery_key=True)
    student_id = db.Column(db.String(20), db.ForeignKey('tbl_students.id'), nullable=True)
    student_marks = db.Column(db.Float, nullable=True)
    std_student_type = db.Column(db.String(50), nullable=True)
    deg_degree_code = db.Column(db.String(10), nullable=True)
    preferance_type = db.Column(db.String(10), nullable=True)
    student_type = db.Column(db.String(10), nullable=True)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())