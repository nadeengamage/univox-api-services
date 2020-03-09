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
from models.NVQStudent import NVQStudent
from models.ALStudent import ALStudent
from schemas.StdMarkSchema import StdMarkSchema
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy import exc

stdmark_schema = StdMarkSchema()
stdmarks_schema = StdMarkSchema(many=True)

# get all applicants marks
@app.route('/applicants/marks', methods=['GET'])
@jwt_required()
def get_stds_marks():
    std_marks = StdMarks.query.all()
    return {'data': stdmarks_schema.dump(std_marks)}, 200

# get marks by student id
@app.route('/applicants/marks/<code>', methods=['GET'])
@jwt_required()
def get_std_marks_by_id(code):
    stds_marks = StdMarks.query.filter_by(student_id=code).first()

    if not stds_marks:
        return {'message': 'Data not found!'}, 200    

    return {'data': stdmark_schema.dump(stds_marks)}, 200

# create an applicant marks
@app.route('/applicants/marks', methods=['POST'])
@jwt_required()
def create_std_marks():
    try:
        payload = request.get_json()
        student_type = payload['student_type'].upper()
        application_no = payload['application_no'].upper()

        if student_type == "NVQ":
            student = NVQStudent.query.filter_by(application_no=application_no).first()
        elif student_type == "AL":
            student = ALStudent.query.filter_by(application_no=application_no).first()
        else:
            return jsonify({'error' : 'Invalid student type!'}), 400

        degree = Degree.query.filter_by(degree_code=payload['degree_code'].upper()).first()

        std_marks = StdMarks(
                    student_id = student.student_id,
                    degree_id = degree.student_id,
                    marks = payload['marks'],
                    remark = payload['remark'],
                    status = 1,
                    created_by = 'admin')
        db.session.add(std_marks)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Student Marks already exists!'}), 400
        pass

    return jsonify({'message' : 'New Student Marks has created!'}), 200

# update an student marks
@app.route('/applicants/marks/<code>', methods=['PUT'])
@jwt_required()
def update_std_marks(code):
    std_marks = StdMarks.query.filter_by(student_id=code).first()
    if not std_marks:
        return {'message': 'Data not found!'}, 200
    else:
        payload = request.get_json()

        try:
            std_marks.marks = payload['marks']
            std_marks.remark = payload['remark']
            std_marks.status = payload['status']
            std_marks.updated_by = 'admin'

            db.session.add(std_marks)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass
        
    return jsonify({'message' : 'Student Marks has been updated!'}), 200


# delete a Student Marks
@app.route('/applicants/marks/<code>', methods=['DELETE'])
@jwt_required()
def delete_std_marks(code):
    std_marks = StdMarks.query.filter_by(student_id=code).first()
    if not std_marks:
        return {'message': 'Data not found!'}, 200
    else:
        try:
            std_marks.status = 0

            db.session.add(std_marks)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass

    return jsonify({'message' : 'Student Marks has been deleted!'}), 200