"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Student Marks Model.
"""

from app import app, db
from models import Student
from models import Degree

class StdMarks(db.Model):
    __tablename__ = 'tbl_students_marks'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column('std_mark_student_id', db.Integer, db.ForeignKey('tbl_students.id'), unique=True, nullable=False)
    #applicant = db.relationship('Student', backref='tbl_students_marks', uselist=False)
    degree_id = db.Column('std_mark_degree_id', db.Integer, db.ForeignKey('tbl_degrees.id'), nullable=False, unique=True)
    #degree = db.relationship('Degree', backref='tbl_students_marks', uselist=False)
    marks = db.Column('std_marks', db.Float, nullable=False)
    remark = db.Column('extra_notice', db.Text)
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


