"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import app, db
from flask import jsonify, request
# from models.NVQReport import NVQReport
# from models.ALReport import ALReport
from services.ReportService import ReportService
from exceptions.validations import ValidationError
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy import exc

service = ReportService()

# get NVQ AL report data
@app.route('/reports', methods=['GET'])
# @jwt_required()
def get_report_data():
    try:
        # payload = request.get_json()

        # if payload['studentType'] == "B1":

        #     if payload['steam'] == "NVQ":
        #         return jsonify({'error' : 'Invalid student type!'}), 400

        #     elif payload['steam'] == "Al":
        #         return jsonify({'error' : 'Invalid student type!'}), 400

        #     elif payload['steam'] == "All":
        #         return jsonify({'error' : 'Invalid student type!'}), 400

        #     else:
        #         return jsonify({'error' : 'Invalid Steam!'}), 400

        # elif payload['studentType'] == "B2":
        #     return jsonify({'error' : 'Invalid student type!'}), 400

        # else:
        #     return jsonify({'error' : 'Invalid student type!'}), 400

        service.generate_nvq_report()

    except ValidationError as e:
        return jsonify({'error': str(e)}), 400