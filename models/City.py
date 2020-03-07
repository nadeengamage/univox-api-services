"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - City Model.
"""

from app import app, db
# from models.District import District

class City(db.Model):
    __tablename__ = 'tbl_cities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    district_id = db.Column('cities_district_id',db.Integer,db.ForeignKey('tbl_districts.id'), nullable=False)
    # district = db.relationship('District', backref='tbl_cities', uselist=False)
    city_code = db.Column(db.String(10), unique=True)
    city_name = db.Column(db.String(50), unique=True)
    postal_code = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
