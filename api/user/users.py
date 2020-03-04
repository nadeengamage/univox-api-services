"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - User controller.
"""

from app import app, db
from flask import jsonify, request
from models.User import User
from schemas.UserSchema import UserSchema, extractor
from services.auth import get_auth_user
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy import exc
import uuid

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# get all roles
@app.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    users = User.query.filter_by(status=1).all()
    return {'data': users_schema.dump(users)}, 200

# get by id
@app.route('/users/<x_id>', methods=['GET'])
@jwt_required()
def get_user_by_x_id(x_id):
    user = User.query.filter_by(x_id=x_id).first()

    if not user:
        return {'message': 'Data not found!'}, 200    

    return {'data': user_schema.dump(user)}, 200

# create an user
@app.route('/users', methods=['POST'])
@app.validate( 'users', 'users')
@jwt_required()
def create_user():
    try:
        payload = request.get_json()
        user =  User(x_id = str(uuid.uuid4()),
                    username = payload['username'],
                    password = payload['password'],
                    firstname = payload['firstname'],
                    lastname = payload['lastname'],
                    role_id = payload['role'],
                    status = 1)
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({'error' : 'User already exists!'}), 400
        pass

    return jsonify({'message' : 'New user created!'}), 200

# update an user
@app.route('/users/<x_id>', methods=['PUT'])
@app.validate( 'users', 'users')
@jwt_required()
def update_user(x_id):
    user = User.query.filter_by(x_id=x_id).first()
    
    if not user: 
        return {'message': 'Data not found!'}, 200 
    else:
        payload = request.get_json()

        try:
            user.username = payload['username']
            user.password = payload['password']
            user.firstname = payload['firstname']
            user.lastname = payload['lastname']
            user.role_id = payload['role']
            user.status = payload['status']

            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass
        

    return jsonify({'message' : 'User updated!'}), 200

# delete user
@app.route('/users/<x_id>', methods=['DELETE'])
@jwt_required()
def delete_user(x_id):
    user = User.query.filter_by(x_id=x_id).first()
    if not user: 
        return {'message': 'Data not found!'}, 200 
    else:
        payload = request.get_json()
        try:
            user.status = payload['status']

            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!'}), 400
            pass

    return jsonify({'message' : 'User deleted!'}), 200
