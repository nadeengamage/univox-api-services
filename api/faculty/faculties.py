"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Faculty.
"""

from app import app, db
from flask import jsonify, request
from models.Faculty import Faculty
from schemas.FacultySchema import FacultySchema
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy import exc

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

# get all faculties
@app.route('/faculties', methods=['GET'])
@jwt_required()
def get_faculties():
    faculties = Faculty.query.filter_by(status=1).all()
    return {'data': faculties_schema.dump(faculties)}, 200

# get by id
@app.route('/faculties/<code>', methods=['GET'])
@jwt_required()
def get_faculty_by_code(code):
    faculty = Faculty.query.filter_by(faculty_code=code.upper()).first()

    if not faculty:
        return {'message': 'Data not found!'}, 200    

    return {'data': faculty_schema.dump(faculty)}, 200

# create an faculty
@app.route('/faculties', methods=['POST'])
@jwt_required()
def create_faculty():
    try:
        payload = request.get_json()
        faculty =  Faculty(
                    faculty_code = payload['faculty_code'].upper(),
                    faculty_name = payload['faculty_name'],
                    status = 1,
                    created_by = 'admin')

        db.session.add(faculty)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Faculty already exists!'}), 400
        pass

    return jsonify({'message' : 'New faculty has created!'}), 200

# update an faculty
@app.route('/faculties/<code>', methods=['PUT'])
@jwt_required()
def update_faculty(code):
    faculty = Faculty.query.filter_by(faculty_code=code.upper()).first()
    
    if not faculty: 
        return {'message': 'Data not found!'}, 200 
    else:
        payload = request.get_json()

        try:
            Faculty.faculty_code = payload['faculty_code'].upper()
            Faculty.faculty_name = payload['faculty_name']
            Faculty.status = payload['status']
            Faculty.updated_by = 'admin'

            db.session.add(faculty)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass
        

    return jsonify({'message' : 'faculty has been updated!'}), 200

# delete faculty
@app.route('/faculties/<code>', methods=['DELETE'])
@jwt_required()
def delete_faculty(code):
    faculty = Faculty.query.filter_by(faculty_code=code.upper()).first()
    if not faculty: 
        return {'message': 'Data not found!'}, 200 
    else:
        try:
            faculty.status = 0

            db.session.add(faculty)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass

    return jsonify({'message' : 'faculty has been deleted!'}), 200