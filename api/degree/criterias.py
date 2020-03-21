"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application criterias.
"""

from app import app, db
from flask import jsonify, request
from models.Criteria import Criteria
from models.Degree import Degree
from schemas.CriteriaSchema import CriteriaSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

criteria_schema = CriteriaSchema()
criterias_schema = CriteriaSchema(many=True)

# get all criterias
@app.route('/criterias', methods=['GET'])
@jwt_required
def get_criterias():
    criterias = Criteria.query.filter_by(status=1).all()
    return {'data': criterias_schema.dump(criterias)}, 200

# get by id
@app.route('/criterias/<code>', methods=['GET'])
@jwt_required
def get_criteria_by_code(code):
    degree = Degree.query.filter_by(degree_code=code.upper()).first()

    if not degree:
        return {'message': 'Data not found!'}, 200
    else:
        criteria = Criteria.query.filter_by(degree_id=degree.id).first()

        if not criteria:
            return {'message': 'Data not found!'}, 200    

    return {'data': criteria_schema.dump(criteria)}, 200

# create an criteria
@app.route('/criterias', methods=['POST'])
@jwt_required
def create_criteria():
    try:
        payload = request.get_json()

        degree = Degree.query.filter_by(degree_code=payload['degree_code'].upper()).first()

        if not degree:
            return {'message': 'Data not found!'}, 200

        criteria =  Criteria(
                    degree_id = degree.id,
                    btch_one_stud_per_program = payload['btch_one_stud_per_program'],
                    btch_two_stud_per_program = payload['btch_two_stud_per_program'],
                    first_exam_paper_mark = payload['first_exam_paper_mark'],
                    second_exam_paper_mark = payload['second_exam_paper_mark'],
                    btch_one_cut_off_mark = payload['btch_one_cut_off_mark'],
                    btch_two_cut_off_mark = payload['btch_two_cut_off_mark'],
                    status = 1,
                    created_by = get_jwt_identity())
        db.session.add(criteria)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'Criteria already exists!'}), 400
        pass

    return jsonify({'message' : 'New criteria has created!'}), 200

# update an criteria
@app.route('/criterias/<code>', methods=['PUT'])
@jwt_required
def update_criteria(code):
    degree = Degree.query.filter_by(degree_code=code.upper()).first()

    if not degree:
        return {'message': 'Data not found!'}, 200
    else:
        criteria = Criteria.query.filter_by(degree_id=degree.id).first()
        
        if not criteria: 
            return {'message': 'Data not found!'}, 200 
        else:
            payload = request.get_json()

            try:
                criteria.degree_id = degree.id
                criteria.btch_one_stud_per_program = payload['btch_one_stud_per_program']
                criteria.btch_two_stud_per_program = payload['btch_two_stud_per_program']
                criteria.first_exam_paper_mark = payload['first_exam_paper_mark']
                criteria.second_exam_paper_mark = payload['second_exam_paper_mark']
                criteria.btch_one_cut_off_mark = payload['btch_one_cut_off_mark']
                criteria.btch_two_cut_off_mark = payload['btch_two_cut_off_mark']
                criteria.status = payload['status']
                criteria.updated_by = get_jwt_identity()

                db.session.add(criteria)
                db.session.commit()
            except exc.IntegrityError:
                db.session().rollback()
                return jsonify({'error' : 'Something error!'}), 400
                pass

    return jsonify({'message' : 'Criteria has been updated!'}), 200

# delete criteria
@app.route('/criterias/<code>', methods=['DELETE'])
@jwt_required
def delete_criteria(code):
    degree = Degree.query.filter_by(degree_code=code.upper()).first()

    if not degree:
        return {'message': 'Data not found!'}, 200
    else:
        criteria = Criteria.query.filter_by(degree_id=degree.id).first()
        if not criteria: 
            return {'message': 'Data not found!'}, 200 
        else:
            try:
                criteria.status = 0
                criteria.updated_by = get_jwt_identity()
                db.session.add(criteria)
                db.session.commit()
            except exc.IntegrityError:
                db.session().rollback()
                return jsonify({'error' : 'Something error!'}), 400
                pass

    return jsonify({'message' : 'Criteria has been deleted!'}), 200