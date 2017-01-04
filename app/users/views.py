# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify
from flask_restful import Resource, Api, fields, marshal_with
from app.events.models import *
import json
from app import db

users = Blueprint('users', __name__)
api = Api()
api.init_app(users)


class Users(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self, type_id):
        pass


api.add_resource(Users, '/', '/<int:user_id>')
