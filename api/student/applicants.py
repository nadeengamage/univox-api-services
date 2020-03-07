"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Applicants Details.
"""

from app import app, db
from flask import jsonify, request
from models.Student import Student
from models.NVQStudent import NVQStudent
from models.ALStudent import ALStudent
from schemas.StudentSchema import StudentSchema
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy import exc
import io
import csv

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# get all applicants
@app.route('/applicants', methods=['GET'])
@jwt_required()
def get_applicants():
    applicants = Student.query.filter_by(status=1).all()
    return {'data': students_schema.dump(applicants)}, 200

# get by id
@app.route('/applicants/<code>', methods=['GET'])
@jwt_required()
def get_student_by_code(code):
    degree = Student.query.filter_by(student_code=code).first()

    if not degree:
        return {'message': 'Data not found!'}, 200    

    return {'data': student_schema.dump(degree)}, 200

# create an degree
@app.route('/applicants', methods=['POST'])
@jwt_required()
def create_applicant():
    try:
        payload = request.get_json()
        student_type = payload['student_type'].upper()
        applicant =  Student(
                        application_no = payload['application_no'].upper(),
                        identity_no = payload['identity_no'].upper(),
                        student_type = student_type,
                        initials = payload['initials'].upper(),
                        surename = payload['surename'].upper(),
                        title = payload['title'],
                        gender = payload['gender'],
                        ethnicity = payload['ethnicity'],
                        address_1 = payload['address_1'],
                        address_2 = payload['address_2'],
                        city = payload['city'],
                        district = payload['district'],
                        telephone = payload['telephone'],
                        mobile = payload['mobile'],
                        email = payload['email'],
                        preference_1 = payload['preference_1'],
                        preference_2 = payload['preference_2'],
                        preference_3 = payload['preference_3'],
                        status = 1,
                        created_by = 'admin')

        db.session.add(applicant)
        db.session.flush()
        db.session.refresh(applicant)
        if student_type == "NVQ":
            nvq_student = NVQStudent(student_id = applicant.id,
                                    index_no = payload['index_no'],
                                    diploma = payload['diploma'],
                                    remarks = payload['remarks'],
                                    permenent_address = payload['permenent_address'],
                                    created_by = 'admin')
            db.session.add(nvq_student)
        elif student_type == "AL":
            al_student = ALStudent(student_id = applicant.id,
                                    stream = payload['stream'],
                                    al_index_no = payload['al_index_no'],
                                    z_score = payload['z_score'],
                                    al_ict = payload['al_ict'],
                                    comm_and_media = payload['comm_and_media'],
                                    general_english = payload['general_english'],
                                    general_common_test = payload['general_common_test'],
                                    created_by = 'admin')
            db.session.add(al_student)
        else:
            return jsonify({'error' : 'Invalid student type!'}), 400

        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Applicant already exists!'}), 400
        pass

    return jsonify({'message' : 'New applicant has created!'}), 200

# create a student
@app.route('/applicants/nvq_students', methods=["POST"])
def funcname():
    input_file = request.files['data_file']
    applicant_details = []
    if not input_file:
        return "Can't find file!"
    
    stream = io.StringIO(input_file.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    print(csv_input)
    for row in csv_input:
        applicant_details = (row)
        
        print(applicant_details[0])
    return "Done"
        # applicant =  Student(
        #                 application_no = payload['application_no'].upper(),
        #                 identity_no = payload['identity_no'].upper(),
        #                 student_type = student_type,
        #                 initials = payload['initials'].upper(),
        #                 surename = payload['surename'].upper(),
        #                 title = payload['title'],
        #                 gender = payload['gender'],
        #                 ethnicity = payload['ethnicity'],
        #                 address_1 = payload['address_1'],
        #                 address_2 = payload['address_2'],
        #                 city = payload['city'],
        #                 district = payload['district'],
        #                 telephone = payload['telephone'],
        #                 mobile = payload['mobile'],
        #                 email = payload['email'],
        #                 preference_1 = payload['preference_1'],
        #                 preference_2 = payload['preference_2'],
        #                 preference_3 = payload['preference_3'],
        #                 status = 1,
        #                 created_by = 'admin')

        # db.session.add(applicant)
        # db.session.flush()
        # db.session.refresh(applicant)
        # if student_type == "NVQ":
        #     nvq_student = NVQStudent(student_id = applicant.id,
        #                             index_no = payload['index_no'],
        #                             diploma = payload['diploma'],
        #                             remarks = payload['remarks'],
        #                             permenent_address = payload['permenent_address'],
        #                             created_by = 'admin')
        #     db.session.add(nvq_student)
        # elif student_type == "AL":
        #     al_student = ALStudent(student_id = applicant.id,
        #                             stream = payload['stream'],
        #                             al_index_no = payload['al_index_no'],
        #                             z_score = payload['z_score'],
        #                             al_ict = payload['al_ict'],
        #                             comm_and_media = payload['comm_and_media'],
        #                             general_english = payload['general_english'],
        #                             general_common_test = payload['general_common_test'],
        #                             created_by = 'admin')
        #     db.session.add(al_student)
        # else:
        #     return jsonify({'error' : 'Invalid student type!'}), 400
    pass