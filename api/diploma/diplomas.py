"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - diploma Controller.
"""

from app import app, db
from flask import jsonify, request
from models.Diploma import Diploma
from schemas.DiplomaSchema import DiplomaSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

diploma_schema = DiplomaSchema()
diplomas_schema = DiplomaSchema(many=True)

# get all diploma
@app.route('/diplomas', methods=['GET'])
@jwt_required
def get_diplomas():
    diplomas = Diploma.query.all()
    return {'data': diplomas_schema.dump(diplomas),'status': 200}, 200

# get by id
@app.route('/diplomas/<code>', methods=['GET'])
@jwt_required
def get_diploma_by_code(code):
    diploma = Diploma.query.filter_by(dip_code=code.upper()).first()

    if not diploma:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': diploma_schema.dump(diploma),'status': 200}, 200

# create an diploma
@app.route('/diplomas', methods=['POST'])
@jwt_required
def create_diploma():
    try:
        payload = request.get_json()

        diploma = Diploma(
                    dip_code = payload['dip_code'].upper(),
                    dip_name = payload['dip_name'],
                    duration = payload['duration'],
                    status = 1,
                    created_by = get_jwt_identity())
        db.session.add(diploma)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Diploma already exists!','status': 400}), 400
        pass

    return jsonify({'message' : 'New Diploma has created!','status': 200}), 200

# update an diploma
@app.route('/diplomas/<code>', methods=['PUT'])
@jwt_required
def update_diploma(code):
    diploma = Diploma.query.filter_by(dip_code=code.upper()).first()
    if not diploma:
        return {'message': 'Data not found!','status': 404}, 404
    else:
        payload = request.get_json()

        try:
            diploma.dip_code = payload['dip_code'].upper()
            diploma.dip_name = payload['dip_name']
            diploma.duration = payload['duration']
            diploma.status = payload['status']
            diploma.updated_by = get_jwt_identity()

            db.session.add(diploma)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass
        
    return jsonify({'message' : 'Diploma has been updated!','status': 200}), 200

# delete an diploma
@app.route('/diplomas/<code>', methods=['DELETE'])
@jwt_required
def delete_diploma(code):
    diploma = Diploma.query.filter_by(dip_code=code.upper()).first()
    if not diploma:
        return {'message': 'Data not found!','status': 404}, 404
    else:
        try:
            db.session.delete(diploma)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

    return jsonify({'message' : 'Diploma has been deleted!','status': 200}), 200
