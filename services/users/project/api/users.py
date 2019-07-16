from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import User
from sqlalchemy import exc

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

class UsersPing(Resource):
    def get(self):
        return {'status': 'success',
            'message': 'pong!'}

class UsersList(Resource):
    def post(self):
        post_data = request.get_json()
        response_object = {'status': 'fail',
            'message': 'Invalid payload.'}
        if not post_data:
            return response_object, 400
        username = post_data.get('username')
        email = post_data.get('email')
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                db.session.add(User(username=username, email=email))
                db.session.commit()
                response_object['status'] = 'success'
                response_object['message'] = f'{email} was added!'
                return response_object, 201
            else:
                response_object['message'] = 'Sorry. That email already exists.'
                return response_object, 400
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400

api.add_resource(UsersPing, '/users/ping')
api.add_resource(UsersList, '/users')
