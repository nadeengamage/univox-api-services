"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX
    
    Description - Students Marks Controller.
"""

from app import app, db
from flask import jsonify, request
from models.StdMarks import StdMarks
from models.Student import Student
from models.Degree import Degree
from models.NVQStudent import NVQStudent
from models.ALStudent import ALStudent
from schemas.StdMarkSchema import StdMarkSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

stdmark_schema = StdMarkSchema()
stdmarks_schema = StdMarkSchema(many=True)

# get all applicants marks
@app.route('/applicants/marks', methods=['GET'])
@jwt_required
def get_stds_marks():
    std_marks = StdMarks.query.all()
    return {'data': stdmarks_schema.dump(std_marks),'status': 200}, 200

# get marks by student id
@app.route('/applicants/marks/<student_type>/<path:code>', methods=['GET'])
@jwt_required
def get_std_marks_by_id(student_type, code):

    if student_type.upper() == "NVQ":
        student = NVQStudent.query.filter_by(application_no=code.upper()).first()
    elif student_type.upper() == "AL":
        student = ALStudent.query.filter_by(application_no=code.upper()).first()
    else:
        return jsonify({'error' : 'Invalid student type!','status': 400}), 400
            
    stds_marks = StdMarks.query.filter_by(student_id=student.id).first()

    if not stds_marks:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': stdmark_schema.dump(stds_marks),'status': 200}, 200

# create an applicant marks
@app.route('/applicants/marks', methods=['POST'])
@jwt_required
def create_std_marks():
    try:
        payload = request.get_json()
        student_type = payload['student_type'].upper()
        application_no = payload['applicant_no'].upper()

        if student_type == "NVQ":
            student = NVQStudent.query.filter_by(application_no=application_no).first()
        elif student_type == "AL":
            student = ALStudent.query.filter_by(application_no=application_no).first()
        else:
            return jsonify({'error' : 'Invalid student type!','status': 400}), 400

        if not student:
            return jsonify({'error' : 'Invalid applicant number!','status': 400}), 400

        std_marks = StdMarks(
                    student_id = student.student_id,
                    marks = payload['marks'],
                    remark = payload['remark'],
                    status = 1,
                    created_by = get_jwt_identity())
        db.session.add(std_marks)
        db.session.commit()
    except exc.IntegrityError as e:
        db.session().rollback()
        if '1062' in str(e.args):
            return jsonify({'error' : 'Marks already entered!','status': 400}), 400
        else:
            return jsonify({'error' : str(e.args),'status': 400}), 400
        pass

    return jsonify({'message' : 'New Student Marks has created!','status': 200}), 200

# update an student marks
@app.route('/applicants/marks', methods=['PUT'])
@jwt_required
def update_std_marks():

    payload = request.get_json()
    student_type = payload['student_type'].upper()
    application_no = payload['applicant_no'].upper()

    if student_type.upper() == "NVQ":
        student = NVQStudent.query.filter_by(application_no=application_no.upper()).first()
        std_marks = StdMarks.query.filter_by(student_id=student.student_id).first()
    elif student_type.upper() == "AL":
        student = ALStudent.query.filter_by(application_no=application_no.upper()).first()
        std_marks = StdMarks.query.filter_by(student_id=student.student_id).first()
    else:
        return jsonify({'error' : 'Invalid student type!','status': 400}), 400

    if not student:
            return jsonify({'error' : 'Invalid applicant number!','status': 400}), 400

    if not std_marks:
        return {'message': 'Data not found!','status': 404}, 404
    else:
        payload = request.get_json()

        try:
            std_marks.marks = payload['marks']
            std_marks.remark = payload['remark']
            std_marks.status = payload['status']
            std_marks.updated_by = get_jwt_identity()

            db.session.add(std_marks)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass
        
    return jsonify({'message' : 'Student Marks has been updated!','status': 200}), 200


# delete a Student Marks
@app.route('/applicants/marks/<student_type>/<path:code>', methods=['DELETE'])
@jwt_required
def delete_std_marks(student_type, code):

    if student_type.upper() == "NVQ":
        student = NVQStudent.query.filter_by(application_no=code.upper()).first()
    elif student_type.upper() == "AL":
        student = ALStudent.query.filter_by(application_no=code.upper()).first()
    else:
        return jsonify({'error' : 'Invalid student type!','status': 400}), 400

    std_marks = StdMarks.query.filter_by(student_id=student.id).first()
    if not std_marks:
        return {'message': 'Data not found!','status': 404}, 404
    else:
        try:
            std_marks.status = 0
            std_marks.updated_by = get_jwt_identity()
            db.session.add(std_marks)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

    return jsonify({'message' : 'Student Marks has been deleted!','status': 200}), 200