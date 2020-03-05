"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - District Model.
"""

from app import app, db

class District(db.Model):
    __tablename__ = 'tbl_districts'

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer)
    district_code = db.Column(db.String(10), unique=True)
    district_name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, district_code):
        self.district_code = district_code
        pass
