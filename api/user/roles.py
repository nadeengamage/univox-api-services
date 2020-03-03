from app import app
from models.Role import Role
from flask import jsonify 

@app.route('/roles')
def get_roles():
    return {'data': Role.query.all()}