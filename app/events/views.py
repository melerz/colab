# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify
from flask_restful import Resource, Api, fields, marshal_with
from app.events.models import *
import json
from app import db

events = Blueprint('events', __name__)
api = Api()
api.init_app(events)

event_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'job': fields.String,
    'team': fields.Integer,
    'picture': fields.String,
    'works_on': fields.Integer,
    'counter': fields.String,
    'name': fields.String,
    'password': fields.Integer,
    'location': fields.Integer
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
        pass

    def delete(self,event_id):
        event = Event.query.get(event_id)
        db.session.delete(event)


resource_fields = {
    'id': fields.String,
    'name': fields.String
}


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
       pass


api.add_resource(Events, '/', '/<int:event_id>')
api.add_resource(EventsType, '/type', '/type/<int:type_id>')
