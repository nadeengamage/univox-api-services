"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Country Model.
"""

from app import app, db

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(10), unique=True)
    country_iso = db.Column(db.String(10), unique=True)
    country_name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def __init__(self, country_code, country_iso):
        self.country_code = country_code
        self.country_iso = country_iso
        pass
