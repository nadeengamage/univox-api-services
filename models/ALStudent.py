"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - AL Applicant Details.
"""

from app import app, db
from models import Student

class ALStudent(db.Model):
    __tablename__ = 'tbl_student_al_details'

    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column('std_al_student_id', db.Integer, db.ForeignKey('tbl_students.id'), unique=True)
    application_no = db.Column('std_application_no', db.String(100), unique=True)
    applicant = db.relationship('Student', backref='tbl_student_al_details', uselist=False)
    stream = db.Column('std_al_stream', db.String(50), unique=True)
    al_index_no = db.Column('std_al_index', db.String(50))
    z_score = db.Column('std_al_z_score', db.String(20))
    al_ict = db.Column('std_al_ict_grade', db.String(5))
    comm_and_media = db.Column('std_comm_and_media_grade', db.String(5))
    general_english = db.Column('std_al_gen_english_grade', db.String(5))
    general_common_test = db.Column('std_al_gen_comm_grede', db.Integer)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
