# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify
from flask_restful import Resource, Api, fields, marshal_with
from app.events.models import *
import json
from app import db
from datetime import datetime

events = Blueprint('events', __name__)
api = Api()
api.init_app(events)

event_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'x_cord': fields.Integer,
    'y_cord': fields.Integer,
    'radius': fields.String,
    'event_type': fields.Integer,
    'created_date': fields.String,
    'urgency': fields.Integer
}


class Events(Resource):
    @marshal_with(event_fields)
    def get(self, event_id=None):
        if event_id:
            events = Event.query.filter(Event.id == event_id).all()
        else:
            events = Event.query.all()
        return events

    def post(self):
        data = request.get_json()
        print(data)
        new_event = Event(data['description'], data['coordinates'], data['radius'], data['event_type'],
                          data['created_by'], data['urgency'])
        db.session.add(new_event)
        db.session.commit()
        return {"result": "success"}, 201

    def delete(self, event_id):
        event = Event.query.get(event_id)
        db.session.delete(event)


resource_fields = {
    'id': fields.Integer,
    'name': fields.String
}

user_json = {
    'id': fields.Integer,
    'user_name': fields.String,
    'job': fields.String,
    'picture': fields.String,
    'works_on': fields.String,
    'country:': fields.String,
    'name': fields.String,
    'password': fields.String,
    'location': fields.Integer,
    'team': fields.String

}


class EventsTypesRelationship(Resource):
    @marshal_with(event_fields)
    def get_all_events_by_type(self, type_id):
        all_events = EventType.get(type_id)
        return all_events.events.all()


class EventsUsersRelationship(Resource):
    @marshal_with(user_json)
    def get_all_users_by_event(self, event_id):
        all_users = Event.get(event_id)
        return all_users.users.all()


class EventsType(Resource):
    @marshal_with(resource_fields)
    def get(self, type_id=None):
        if type_id:
            events_types = EventType.query.filter(EventType.id == type_id).all()
        else:
            events_types = EventType.query.all()
        return events_types

    def post(self):
        data = request.get_json()
        ev = EventType(data['name'])
        db.session.add(ev)
        db.session.commit()
        return {"result": "success"}, 201

    def delete(self, type_id):
        event = EventType.query.filter(EventType.id == type_id).first()
        db.session.delete(event)


api.add_resource(Events, '/', '/<int:event_id>')
api.add_resource(EventsUsersRelationship, '/<int:event_id>')
api.add_resource(EventsType, '/type', '/type/<int:type_id>')
api.add_resource(EventsTypesRelationship, '/type/<int:type_id>')
