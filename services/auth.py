"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Authentication Service
"""
from app import app
from models.User import User
from werkzeug.security import safe_str_cmp
from flask import request
import jwt

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)

def get_auth_user():
    token = request.headers.get('Authorization')
    data = jwt.decode(token, app.config['SECRET_KEY'], 'utf-8', algorithms=['HS256'])
    return User.query.filter_by(id=data['identity']).first()