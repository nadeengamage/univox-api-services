"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Application degrees.
"""

from app import app, db
from flask import jsonify, request
from models.Degree import Degree
from models.Faculty import Faculty
from schemas.DegreeSchema import DegreeSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

degree_schema = DegreeSchema()
degrees_schema = DegreeSchema(many=True)

# get all degrees
@app.route('/degrees', methods=['GET'])
@jwt_required
def get_degrees():
    degrees = Degree.query.filter_by().all()
    return {'data': degrees_schema.dump(degrees),'status': 200}, 200

# get by id
@app.route('/degrees/<code>', methods=['GET'])
@jwt_required
def get_degree_by_code(code):
    degree = Degree.query.filter_by(degree_code=code).first()

    if not degree:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': degree_schema.dump(degree),'status': 200}, 200

# create an degree
@app.route('/degrees', methods=['POST'])
@jwt_required
def create_degree():
    try:
        payload = request.get_json()

        faculty = Faculty.query.filter_by(faculty_code=payload['faculty_code']).first()

        if not faculty:
            return {'message': 'Faculty data not found!','status': 404}, 404 

        degree =  Degree(
                    faculty_id = faculty.id,
                    degree_code = payload['degree_code'].upper(),
                    degree_name = payload['degree_name'],
                    status = 1,
                    created_by = get_jwt_identity())
        db.session.add(degree)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Degree already exists!','status': 400}), 400
        pass

    return jsonify({'message' : 'New degree has created!','status': 200}), 200

# update an degree
@app.route('/degrees/<code>', methods=['PUT'])
@jwt_required
def update_degree(code):
    degree = Degree.query.filter_by(degree_code=code).first()
    
    if not degree: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        payload = request.get_json()

        try:

            faculty = Faculty.query.filter_by(faculty_code=payload['faculty_code']).first()

            degree.faculty_id = faculty.id
            degree.degree_code = payload['degree_code']
            degree.degree_name = payload['degree_name']
            degree.status = payload['status']
            degree.updated_by = get_jwt_identity()

            db.session.add(degree)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass
        

    return jsonify({'message' : 'Degree has been updated!','status': 200}), 200

# delete degree
@app.route('/degrees/<code>', methods=['DELETE'])
@jwt_required
def delete_degree(code):
    degree = Degree.query.filter_by(degree_code=code.upper()).first()
    if not degree: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        try:
            db.session.delete(degree)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

    return jsonify({'message' : 'Degree has been deleted!','status': 200}), 200