"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Criteria.
"""

from app import app, db
# from models.Degree import Degree

class Criteria(db.Model):
    __tablename__ = 'tbl_criterias'

    id = db.Column(db.Integer, primary_key=True)
    degree_id = db.Column('crt_degree_id', db.Integer, db.ForeignKey('tbl_degrees.id'), nullable=False, unique=True)
    degree = db.relationship('Degree', backref='tbl_criterias', uselist=False)
    btch_one_stud_per_program = db.Column('crt_btch_one_stud_per_program', db.Integer, primary_key=True)
    btch_two_stud_per_program = db.Column('crt_btch_two_stud_per_program', db.Integer, primary_key=True)
    first_exam_paper_mark = db.Column('crt_first_exam_paper_mark', db.String(10), primary_key=True)
    second_exam_paper_mark = db.Column('crt_second_exam_paper_mark', db.String(10), primary_key=True)
    btch_one_cut_off_mark = db.Column('crt_btch_one_cut_off_mark', db.String(10), primary_key=True)
    btch_two_cut_off_mark = db.Column('crt_btch_two_cut_off_mark', db.String(10), primary_key=True)
    status = db.Column(db.Boolean)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())