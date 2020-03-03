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
from flask_jwt import JWT, jwt_required, current_identity
import uuid

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# get all roles
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return {'data': users_schema.dump(users)}, 200

# get by id
@app.route('/users/<x_id>', methods=['GET'])
def get_user_by_x_id(x_id):
    user = User.query.filter_by(x_id=x_id).first()

    if not user:
        return {'message': 'Data not found!'}, 200    

    return {'data': user_schema.dump(user)}, 200

# create an user
@app.route('/users', methods=['POST'])
def create_user():
    payload = request.get_json()
    user =  User(x_id = str(uuid.uuid4()),
                username = payload['username'],
                password = payload['password'],
                firstname = payload['firstname'],
                lastname = payload['lastname'],
                role = payload['role'],
                status = 1)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message' : 'New user created!'})
    