"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application users.
"""

from app import app, db
from models import NVQStudent
from models import ALStudent

class Student(db.Model):
    __tablename__ = 'tbl_students'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nvq_details = db.relationship('NVQStudent', backref='tbl_students', uselist=False)
    al_details = db.relationship('ALStudent', backref='tbl_students', uselist=False)
    identity_no = db.Column('std_identity_no', db.String(20), unique=True, nullable=False)
    student_type = db.Column('std_student_type', db.String(5))
    initials = db.Column('std_initials', db.String(20), nullable=False)
    surename = db.Column('std_surename', db.String(50), nullable=False)
    title = db.Column('std_title', db.String(5), nullable=False)
    gender = db.Column('std_gender', db.String(10), nullable=False)
    ethnicity = db.Column('std_ethnicity', db.String(20), nullable=False)
    marital_status = db.Column('std_marital_status', db.String(5))
    address_1 = db.Column('std_address_1', db.String(100), nullable=False)
    address_2 = db.Column('std_address_2', db.String(100))
    address_3 = db.Column('std_address_3', db.String(100))
    city = db.Column('std_city', db.String(50), nullable=False)
    district = db.Column('std_district', db.String(50), nullable=False)
    permanent_district = db.Column('std_permanent_district', db.String(50), nullable=False)
    telephone = db.Column('std_telephone', db.String(20))
    mobile = db.Column('std_mobile', db.String(20))
    email = db.Column('std_email', db.String(100))
    preference_1 = db.Column('std_preference_1', db.String(10), nullable=False)
    preference_2 = db.Column('std_preference_2', db.String(10))
    preference_3 = db.Column('std_preference_3', db.String(10))
    status = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())