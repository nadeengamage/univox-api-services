"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Role Permissions Controller.
"""


from app import app, db
from flask import jsonify, request
from models.Permission import Permission
from schemas.PermissionSchema import PermissionSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

permission_schema = PermissionSchema()
permissions_schema = PermissionSchema(many=True)

# get all role permission
@app.route('/role/permissions', methods=['GET'])
@jwt_required
def get_all_permissions():
    permissions = Permission.query.filter_by().all()
    return {'data': permissions_schema.dump(permissions),'status': 200}, 200


# get permission by role code
@app.route('/role/permissions/<role_code>', methods=['GET'])
@jwt_required
def get_permission_by_role_code(role_code):
    permission = Permission.query.filter_by(role_code=role_code).first()

    if not permission:
        return {'message': 'Data not found!','status': 404}, 404    

    return {'data': permission_schema.dump(permission),'status': 200}, 200


# create a permission for role
@app.route('/role/permissions', methods=['POST'])
@jwt_required
def create_role_permission():
    payload = request.get_json()

    role = Role.query.filter_by(role_code=payload['role_code']).first()

    if not role:
        return jsonify({'error' : 'Invalid role code!','status': 400}), 400

    try:
        permission = Permission(
                    read = payload['read']
                    write = payload['write']
                    add = payload['add']
                    delete = payload['delete']
                    role_code = role.role_code
                    controller = payload['controller']
                    status = 1
                    updated_by = 'admin')
        db.session.add(permission)
        db.session.commit()
    except exc.IntegrityError as e:
        db.session().rollback()
        return jsonify({'error' : str(e.args),'status': 400}), 400
        pass

    return jsonify({'message' : 'New Role Permission has created!','status': 200}), 200


    # update a permission for role
    @app.route('/role/permissions/<role_code>/<controller>', methods=['PUT'])
    @jwt_required
    def update_role_permission(role_code, controller):
        role = Role.query.filter_by(role_code=role_code).first()

        if not role:
            return jsonify({'error' : 'Invalid role code!','status': 400}), 400

        if controller == "":
            return jsonify({'error' : 'Role controller not fount!','status': 404}), 404

        permission = Permission.query.filter_by(role_code=role_code, controller=controller).first()
        if not permission:
            return {'message': 'Data not found!','status': 404}, 404
        else:
            payload = request.get_json()

        try:

            permission.read = payload['read']
            permission.write = payload['write']
            permission.add = payload['add']
            permission.delete = payload['delete']
            permission.role_code = payload['role_code']
            permission.controller = payload['controller']
            permission.status = payload['status']
            permission.updated_by = get_jwt_identity()

            db.session.add(permission)
            db.session.commit()
        except exc.IntegrityError:
            db.session().rollback()
            return jsonify({'error' : 'Something error!','status': 400}), 400
            pass

        return jsonify({'message' : 'Role Permission updated!','status': 200}), 200