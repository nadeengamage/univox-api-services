"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - District controller.
"""

from app import app
from flask import jsonify
from models.District import District
from schemas.DistrictSchema import DistrictSchema
from flask_jwt import JWT, jwt_required, current_identity

district_schema = DistrictSchema()
districts_schema = DistrictSchema(many=True)

# get all districts
@app.route('/districts', methods=['GET'])
def get_districts():
    districts = District.query.all()
    return {'data': districts_schema.dump(districts)}, 200

# get by district code
@app.route('/districts/<district_code>', methods=['GET'])
@jwt_required()
def get_district_by_code(district_code):
    district = District.query.filter_by(district_code=district_code).first()

    if not district:
        return {'message': 'Data not found!'}, 200

    return {'data': districts_schema.dump(district)}, 200
