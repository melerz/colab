# kernel
from sqlalchemy import Table, Column, Integer, String
from app import db

class Event(db.Model):

    id=db.Column(Integer,primary_key=True)
    type=db.Column(db.String,db.ForeignKey('EventType.id'))
    description = db.Column(db.String(120))
    location = db.Column(Integer) #todo polygon
    createdBy=db.Column(db.String, db.ForeignKey('Users.id'))
    createdDate=db.Column(Integer)
    urgency=db.Column(Integer)

    def __repr__(self):
        return type


class Team(Base):
    id = Column(Integer,primary_key=True)
    key=Column(Integer)
    name=Column(String(25))

    def __init__(self,key,name):
        self.key=key
        self.name=name

    def __repr__(self):
        return '<Team: %r>' %self.name

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    userName=Column(String)
    job=Column(String(30))
    team=Column()
    pic=Column()
