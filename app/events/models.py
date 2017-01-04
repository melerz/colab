# kernel
from sqlalchemy import Table, Column, Integer, String
from app import db

class Event(db.Model):

    id=db.Column(Integer,primary_key=True)
    type=db.Column(db.String,db.ForeignKey('EventType.id'))
    description = db.Column(db.String(120))
    location = db.Column(Integer) #todo polygon
    createdBy=db.Column(db.String, db.ForeignKey('users.id'))
    createdDate=db.Column(Integer)
    urgency=db.Column(Integer)

    def __repr__(self):
        return type
