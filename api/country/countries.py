"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Country controller.
"""

from app import app
from flask import jsonify
from models.Country import Country
from schemas.CountrySchema import CountrySchema
from flask_jwt import JWT, jwt_required, current_identity

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)

#get all countries
@app.route('/countries', methods=['GET'])
# @jwt_required()
def get_countries():
    countries = Country.query.all()
    return {'data': countries_schema.dump(countries)}, 200