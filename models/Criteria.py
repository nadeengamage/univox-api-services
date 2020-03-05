"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Criteria.
"""

from app import app, db

class Criteria(db.Model):
    __tablename__ = 'tbl_criterias'

    id = db.Column(db.Integer, primary_key=True)
    crt_degree_id = db.Column(db.Integer, primary_key=True)
    crt_btch_one_stud_per_program = db.Column(db.Integer, primary_key=True)
    crt_btch_two_stud_per_program = db.Column(db.Integer, primary_key=True)
    crt_first_exam_paper_mark = db.Column(db.DECIMAL, primary_key=True)
    crt_second_exam_paper_mark = db.Column(db.DECIMAL, primary_key=True)
    crt_btch_one_cut_off_mark = db.Column(db.DECIMAL, primary_key=True)
    crt_btch_two_cut_off_mark = db.Column(db.DECIMAL, primary_key=True)
    status = db.Column(db.Boolean)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())