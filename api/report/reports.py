"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import app, db
from flask import jsonify, request
from models.Criteria import Criteria
from models.Degree import Degree
from services.ReportService import ReportService
from exceptions.validations import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

service = ReportService()

BUFFER = 10

# get NVQ/AL report data
@app.route('/reports', methods=['POST'])
@jwt_required
def get_report_data():
    try:
        payload = request.get_json()

        # get criteria by degree code
        degree = Degree.query.filter_by(degree_code=payload['degree'].upper()).first()

        if not degree:
            return {'message': 'Degree not found!'}, 200
        else:
            criteria = Criteria.query.filter_by(degree_id=degree.id).first()

            if not criteria:
                return {'message': 'Criteria not found!'}, 200    

        if payload['batch_type'] == "B1":
            # generate the records
            service.generate_nvq_report("B1", get_jwt_identity())
            service.generate_al_report(get_jwt_identity());

            if payload['stream'] == "NVQ":
                # fetch generated data by the degree code
                result = service.get_nvq_applicants_by_degree_code((criteria.btch_one_stud_per_program + BUFFER), degree.degree_code, "B1")
                return jsonify({'message' : 'NVQ', 'result': [dict(row) for row in result]}), 200

            elif payload['stream'] == "AL":
                # fetch generated data by the degree code
                result = service.get_al_applicants_by_degree_code((criteria.btch_one_stud_per_program + BUFFER), degree.degree_code, "B1")
                return jsonify({'message' : 'AL', 'result': [dict(row) for row in result]}), 200

            elif payload['stream'] == "ALL":
                nvq_result = service.get_nvq_applicants_by_degree_code((criteria.btch_one_stud_per_program + BUFFER), degree.degree_code, "B1")
                nvq_count = len([dict(row) for row in nvq_result])
                
                if (criteria.btch_one_stud_per_program + BUFFER) > nvq_count: 
                    nvq_al_result = service.get_nvq_al_applicants_by_degree_code((nvq_count + BUFFER), ((criteria.btch_one_stud_per_program + BUFFER) - nvq_count), degree.degree_code, "B1")
                    return jsonify({'message' : 'ALL_NVQ_AL', 'result': [dict(row) for row in nvq_al_result]}), 200
                else:
                    result = service.get_nvq_applicants_by_degree_code((criteria.btch_one_stud_per_program + BUFFER), degree.degree_code, "B1")
                    return jsonify({'message' : 'ALL_NVQ', 'result': [dict(row) for row in result]}), 200
            else:
                return jsonify({'error' : 'Invalid stream!'}), 400

        elif payload['batch_type'] == "B2":
            # generate the records
            service.generate_nvq_report("B2", get_jwt_identity())

            # fetch generated data by the degree code
            result = service.get_nvq_applicants_by_degree_code((criteria.btch_two_stud_per_program + BUFFER), degree.degree_code, "B2")
            return jsonify({'message' : 'NVQ', 'result': [dict(row) for row in result]}), 200

        else:
            return jsonify({'error' : 'Invalid Batch Type!'}), 400

    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
