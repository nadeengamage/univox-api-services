"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application degrees.
"""

from app import app, db
from flask import jsonify, request
from models.Degree import Degree
from schemas.DegreeSchema import DegreeSchema
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy import exc

degree_schema = DegreeSchema()
degrees_schema = DegreeSchema(many=True)

# get all degrees
@app.route('/degrees', methods=['GET'])
@jwt_required()
def get_degrees():
    degrees = Degree.query.filter_by(status=1).all()
    return {'data': degrees_schema.dump(degrees)}, 200

# get by id
@app.route('/degrees/<code>', methods=['GET'])
@jwt_required()
def get_degree_by_code(code):
    degree = Degree.query.filter_by(degree_code=code).first()

    if not degree:
        return {'message': 'Data not found!'}, 200    

    return {'data': degree_schema.dump(degree)}, 200

# create an degree
@app.route('/degrees', methods=['POST'])
@jwt_required()
def create_degree():
    try:
        payload = request.get_json()
        degree =  Degree(
                    faculty_id = payload['faculty_id'],
                    degree_code = payload['degree_code'].upper(),
                    degree_name = payload['degree_name'],
                    status = 1,
                    created_by = 'admin')
        db.session.add(degree)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Degree already exists!'}), 400
        pass

    return jsonify({'message' : 'New degree has created!'}), 200

# update an degree
@app.route('/degrees/<code>', methods=['PUT'])
@jwt_required()
def update_degree(code):
    degree = Degree.query.filter_by(degree_code=code).first()
    
    if not degree: 
        return {'message': 'Data not found!'}, 200 
    else:
        payload = request.get_json()

        try:
            degree.faculty_id = payload['faculty_id']
            degree.degree_code = payload['degree_code']
            degree.degree_name = payload['degree_name']
            degree.status = payload['status']
            degree.updated_by = 'admin'

            db.session.add(degree)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass
        

    return jsonify({'message' : 'Degree has been updated!'}), 200

# delete degree
@app.route('/degrees/<code>', methods=['DELETE'])
@jwt_required()
def delete_degree(code):
    degree = Degree.query.filter_by(degree_code=code).first()
    if not degree: 
        return {'message': 'Data not found!'}, 200 
    else:
        try:
            degree.status = 0

            db.session.add(degree)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass

    return jsonify({'message' : 'Degree has been deleted!'}), 200