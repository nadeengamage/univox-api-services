"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import app
from flask import jsonify
from models.Country import Country
from schemas.CountrySchema import CountrySchema
from flask_jwt_extended import jwt_required, get_jwt_identity

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)

#get all countries
@app.route('/countries', methods=['GET'])
@jwt_required
def get_countries():
    countries = Country.query.all()
    return {'data': countries_schema.dump(countries)}, 200