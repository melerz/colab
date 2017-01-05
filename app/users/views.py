# Import flask dependencies
from flask import Blueprint, request
from flask_restful import Resource, Api, fields, marshal_with
from app.users.models import *
from app import db

users = Blueprint('users', __name__)
api = Api()
api.init_app(users)

resource_fields = {
    'id': fields.Integer,
    'user_name': fields.String,
    'job': fields.String,
    'picture': fields.String,
    'works_on': fields.String,
    'country': fields.String,
    'name': fields.String,
    'password': fields.String,
    'location': fields.Integer,
    'team': fields.String

}


class Users(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
        else:
            user = User.query.all()
        return user

    def post(self):
        data = request.get_json()
        user = User(data['user_name'], data['job'], data['picture'], data['works_on'], data['country'], data['name'],
                    data['password'], data['location'], data['team'])
        db.session.add(user)
        db.session.commit()
        return {"result": "success"}, 201

    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

    def put(self, user_id):
        data = request.get_json()
        user = User.query.get(user_id)
        # user.name = data['name']
        # user.user_name = data['user_name']
        # user.job = data['job']
        # user.country = data['country']
        user.team = data['team']
        # user.works_on = data['works_on']
        # user.password = data['password']
        # user.location = data['location']
        # user.picture = data['picture']
        db.session.commit()
        return {"result": "success"}, 201


team_json = {
    'id': fields.Integer,
    'name': fields.String
}


class TeamView(Resource):
    @marshal_with(team_json)
    def get(self, team_id=None):
        if team_id:
            groups = Team.query.filter(Team.id == team_id).all()
        else:
            groups = Team.query.all()
        return groups

    def post(self):
        data = request.get_json()
        team = Team(data['name'])
        db.session.add(team)
        db.session.commit()


class TeamUsersView(Resource):
    @marshal_with(resource_fields)
    def get(self, team_id):
        users = User.query.get(team_id).users
        return users


api.add_resource(Users, '/users', '/users/<int:user_id>')
api.add_resource(TeamView, '/teams', '/teams/<int:team_id>')
api.add_resource(TeamUsersView, '/teams/<int:team_id>/users')
