"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - NVQ Applicant details.
"""

from app import app, db
from models import Student

class NVQStudent(db.Model):
    __tablename__ = 'tbl_student_nvq_details'

    id = db.Column('id',db.Integer, primary_key=True)
    student_id = db.Column('std_nvq_student_id',db.Integer, db.ForeignKey('tbl_students.id'), unique=True, nullable=False)
    application_no = db.Column('std_application_no', db.String(100), unique=True, nullable=False)
    batch_type = db.Column('std_batch_type', db.String(4), unique=True)
    applicant = db.relationship('Student', backref='tbl_student_nvq_details', uselist=False)
    index_no = db.Column('std_nvq_index_no',db.String(50), unique=True)
    diploma = db.Column('std_nvq_diploma',db.String(80))
    remarks = db.Column('std_nvq_remarks',db.String(2000))
    permenent_address = db.Column('std_nvq_permenent_address',db.String(200))
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
