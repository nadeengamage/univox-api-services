"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import app
from flask import jsonify
from models.District import District
from schemas.DistrictSchema import DistrictSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

district_schema = DistrictSchema()
districts_schema = DistrictSchema(many=True)

# get all districts
@app.route('/districts', methods=['GET'])
def get_districts():
    districts = District.query.all()
    return {'data': districts_schema.dump(districts),'status': 200}, 200

# get by district code
@app.route('/districts/<district_code>', methods=['GET'])
@jwt_required
def get_district_by_code(district_code):
    district = District.query.filter_by(district_code=district_code).first()

    if not district:
        return {'message': 'Data not found!','status': 404}, 404

    return {'data': districts_schema.dump(district),'status': 200}, 200
