"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Country Model.
"""

from app import db
from models.District import District

class Country(db.Model):
    __tablename__ = 'tbl_countries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_code = db.Column(db.String(10), unique=True)
    country_iso = db.Column(db.String(10), unique=True)
    country_name = db.Column(db.String(50), unique=True)
    districts = db.relationship('District', backref='tbl_countries', uselist=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
