"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - User schema.
"""

from flask import request
from app import ma
from models.User import User

class UserSchema(ma.Schema):
  class Meta:
    fields = ('x_id', 'username', 'firstname', 'lastname', 'role', 'status')

def extractor():
    payload = request.get_json()
    return User(x_id = str(uuid.uuid4()),
                username = payload['username'],
                password = payload['password'],
                firstname = payload['firstname'],
                lastname = payload['lastname'],
                role = payload['role'],
                status = 1)