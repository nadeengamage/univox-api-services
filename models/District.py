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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column('dist_country_id',db.Integer,db.ForeignKey(tbl_countries.id), nullable=False)
    district_code = db.Column(db.String(10), unique=True)
    district_name = db.Column(db.String(50), unique=True)
    countries = db.relationship('Country', backref='tbl_countries', uselist=False)
    cities = db.relationship('City', backref='tbl_cities', uselist=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, district_code):
        self.district_code = district_code
        pass
