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
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

# get all faculties
@app.route('/faculties', methods=['GET'])
@jwt_required
def get_faculties():
    faculties = Faculty.query.filter_by().all()
    return {'data': faculties_schema.dump(faculties),'status': 200}, 200

# get by id
@app.route('/faculties/<code>', methods=['GET'])
@jwt_required
def get_faculty_by_code(code):

    if not code: 
        return {'message': 'Faculty code is required!','status': 400}, 400 
        
    faculty = Faculty.query.filter_by(faculty_code=code.upper()).first()

    if not faculty:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': faculty_schema.dump(faculty),'status': 200}, 200

# create an faculty
@app.route('/faculties', methods=['POST'])
@jwt_required
def create_faculty():
    try:
        payload = request.get_json()
        faculty =  Faculty(
                    faculty_code = payload['faculty_code'].upper(),
                    faculty_name = payload['faculty_name'],
                    status = 1,
                    created_by = get_jwt_identity())

        db.session.add(faculty)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Faculty already exists!','status': 400}), 400
        pass

    return jsonify({'message' : 'New faculty has created!','status': 200}), 200

# update an faculty
@app.route('/faculties/<code>', methods=['PUT'])
@jwt_required
def update_faculty(code):

    if not code: 
        return {'message': 'Faculty code is required!','status': 400}, 400 

    faculty = Faculty.query.filter_by(faculty_code=code.upper()).first()
    
    if not faculty: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        payload = request.get_json()

        try:
            Faculty.faculty_code = payload['faculty_code'].upper()
            Faculty.faculty_name = payload['faculty_name']
            Faculty.status = payload['status']
            Faculty.updated_by = get_jwt_identity()

            db.session.add(faculty)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass
        

    return jsonify({'message' : 'faculty has been updated!','status': 200}), 200

# delete faculty
@app.route('/faculties/<code>', methods=['DELETE'])
@jwt_required
def delete_faculty(code):

    if not code: 
        return {'message': 'Faculty code is required!','status': 400}, 400 

    faculty = Faculty.query.filter_by(faculty_code=code.upper()).first()
    if not faculty: 
        return {'message': 'Data not found!','status': 404}, 404 
    else:
        try:
            db.session.delete(faculty)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

    return jsonify({'message' : 'Faculty has been deleted!','status': 200}), 200