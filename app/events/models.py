from app import db


class Event(db.Model):
    __tablename__ = "Event"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    coordinates = db.Column(db.Integer)
    radius = db.Column(db.Integer)
    event_type = db.Column(db.Integer, db.ForeignKey('EventType.id'))
    created_by = db.Column(db.Integer, db.ForeignKey('User.id'))
    created_date = db.Column(db.DateTime)
    urgency = db.Column(db.Integer)
    users = db.relationship('User',backref='Event',lazy='dynamic')

    def __repr__(self):
        return self.description

    def __init__(self, description, coordinates, radius, event_type, created_by, created_date, urgency):
        self.description = description
        self.coordinates = coordinates
        self.radius = radius
        self.event_type = event_type
        self.created_by = created_by
        self.created_date = created_date
        self.urgency = urgency


class EventType(db.Model):
    __tablename__ = "EventType"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    events = db.relationship('Event',backref='event_type', lazy='dynamic')

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name

