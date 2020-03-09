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
from services.extractor import extract_nvq_details, extract_al_details
from exceptions.validations import ValidationError
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy import exc
import io
import csv

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# get all nvq applicants
@app.route('/applicants/nvq/details', methods=['GET'])
@jwt_required()
def get_nvq_applicants():
    applicants = Student.query.filter_by(student_type='NVQ').all()
    return {'data': students_schema.dump(applicants)}, 200

# get all al applicants
@app.route('/applicants/al/details', methods=['GET'])
@jwt_required()
def get_al_applicants():
    applicants = Student.query.filter_by(student_type='AL').all()
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
                                    application_no = payload['application_no'].upper(),
                                    index_no = payload['index_no'],
                                    diploma = payload['diploma'],
                                    remarks = payload['remarks'],
                                    permenent_address = payload['permenent_address'],
                                    created_by = 'admin')
            db.session.add(nvq_student)
        elif student_type == "AL":
            al_student = ALStudent(student_id = applicant.id,
                                    application_no = payload['application_no'].upper(),
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

# nvq students bulk import
@app.route('/applicants/transform/nvq_students', methods=["POST"])
@jwt_required()
def create_bulk_import_nvq():
    input_file = request.files['data_file']

    if not input_file:
        return "Can't find a file!"
    
    try:
        stream = io.StringIO(input_file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)

        if not csv_input:
            return jsonify({'error': 'CSV file is required'}), 400

        applicants = extract_nvq_details([row for row in csv_input])  
        for applicant in applicants:
            applicant_details =  Student(
                            identity_no = applicant.get('identity_no'),
                            student_type = 'NVQ',
                            initials = applicant.get('initials'),
                            surename = applicant.get('surename'),
                            title = applicant.get('title'),
                            gender = applicant.get('gender'),
                            ethnicity = applicant.get('ethnicity'),
                            address_1 = applicant.get('address_1'),
                            address_2 = applicant.get('address_2'),
                            city = applicant.get('city'),
                            district = applicant.get('district'),
                            telephone = applicant.get('telephone'),
                            mobile = applicant.get('mobile'),
                            email = applicant.get('email'),
                            preference_1 = applicant.get('preference_1'),
                            preference_2 = applicant.get('preference_2'),
                            preference_3 = applicant.get('preference_3'),
                            status = 1,
                            created_by = 'admin')

            db.session.add(applicant_details)
            db.session.flush()
            db.session.refresh(applicant_details)

            nvq_student = NVQStudent(student_id = applicant_details.id,
                                    application_no = applicant.get('application_no'),
                                    index_no = applicant.get('index_no'),
                                    diploma = applicant.get('diploma'),
                                    remarks = applicant.get('remarks'),
                                    permenent_address = applicant.get('permenent_address'),
                                    created_by = 'admin')
            db.session.add(nvq_student)

            db.session.commit()
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
        pass
    except exc.IntegrityError as e:
        db.session().rollback()
        return jsonify({'error' : str(e.args)}), 400
        pass
    
    return jsonify({'message' : 'Bulk import succeeded!'}), 200

# al student bulk import
@app.route('/applicants/transform/al_students', methods=["POST"])
@jwt_required()
def create_bulk_import_al():
    input_file = request.files['data_file']

    if not input_file:
        return "Can't find a file!"
    
    try:
        stream = io.StringIO(input_file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)

        if not csv_input:
            return jsonify({'error': 'CSV file is required'}), 400

        applicants = extract_al_details([row for row in csv_input])  
        for applicant in applicants:
            applicant_details =  Student(
                            identity_no = applicant.get('identity_no'),
                            student_type = 'AL',
                            initials = applicant.get('initials'),
                            surename = applicant.get('surename'),
                            title = applicant.get('title'),
                            gender = applicant.get('gender'),
                            ethnicity = applicant.get('ethnicity'),
                            address_1 = applicant.get('address_1'),
                            address_2 = applicant.get('address_2'),
                            city = applicant.get('city'),
                            district = applicant.get('district'),
                            telephone = applicant.get('telephone'),
                            mobile = applicant.get('mobile'),
                            email = applicant.get('email'),
                            preference_1 = applicant.get('preference_1'),
                            preference_2 = applicant.get('preference_2'),
                            preference_3 = applicant.get('preference_3'),
                            status = 1,
                            created_by = 'admin')

            db.session.add(applicant_details)
            db.session.flush()
            db.session.refresh(applicant_details)

            al_student = ALStudent(student_id = applicant_details.id,
                                    application_no = applicant.get('application_no'),
                                    stream = applicant.get('stream'),
                                    al_index_no = applicant.get('al_index_no'),
                                    z_score = applicant.get('z_score'),
                                    al_ict = applicant.get('al_ict_grade'),
                                    comm_and_media = applicant.get('comm_media_grade'),
                                    general_english = applicant.get('gen_eng_grade'),
                                    general_common_test = applicant.get('com_gen_test_grade'),
                                    created_by = 'admin')
            db.session.add(al_student)

            db.session.commit()
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
        pass
    except exc.IntegrityError as e:
        db.session().rollback()
        return jsonify({'error' : str(e.args)}), 400
        pass
    
    return jsonify({'message' : 'Bulk import succeeded!'}), 200