"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import app
from flask import jsonify
from models.City import City
from schemas.CitySchema import CitySchema
from flask_jwt_extended import jwt_required, get_jwt_identity

city_schema = CitySchema()
cities_schema = CitySchema(many=True)

# get all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    cities = City.query.all()
    return {'data': cities_schema.dump(cities),'status': 200}, 200

# get by cities code
@app.route('/cities/<city_code>', methods=['GET'])
@jwt_required
def get_cities_by_code(city_code):
    city = City.query.filter_by(city_code=city_code).first()

    if not city:
        return {'message': 'Data not found!','status': 404}, 404

    return {'data': cities_schema.dump(city),'status': 200}, 200