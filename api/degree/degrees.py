"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application users.
"""

from app import app
from flask import jsonify
from models.Degree import Degree
from schemas.DegreeSchema import DegreeSchema
from flask_jwt import JWT, jwt_required, current_identity

degree_schema = DegreeSchema()
degrees_schema = DegreeSchema(many=True)

# get all degrees
@app.route('/degrees')
@jwt_required()
def get_degrees():
    degrees = Degree.query.all()
    return {'data': degree_schema.dump(degrees)}, 200

