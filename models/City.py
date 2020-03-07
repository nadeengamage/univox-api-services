"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - City Model.
"""

from app import app, db

class City(db.Model):
    __tablename__ = 'tbl_cities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    district_id = db.Column('cities_district_id',db.Integer,db.ForeignKey(tbl_districts.id), nullable=False)
    city_code = db.Column(db.String(10), unique=True)
    city_name = db.Column(db.String(50), unique=True)
    postal_code = db.Column(db.Integer)
    districts = db.relationship('District', backref='tbl_districts', uselist=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, city_code, postal_code):
        self.city_code = city_code
        self.postal_code = postal_code
        pass