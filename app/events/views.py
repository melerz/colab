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

resource_fields = {
    'id': fields.String,
    'name': fields.String
}


class Events(Resource):
    def get(self):
        return "im in get api for events"

    def post(self):
        return "post created succefully"

    def delete(self):
        return "post created succefully"

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


api.add_resource(Events, '/')
api.add_resource(EventsType, '/type', '/type/<int:type_id>')
