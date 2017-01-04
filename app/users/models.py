from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String,unique=True)
    job = db.Column(db.String(30))
    team = db.Column(db.Integer, db.ForgeinKey('Team.id'))
    pic = db.Column(db.Integer, db.ForgeinKey('Pics.id'))

    def __repr__(self):
        return self.userName

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)

    def __repr__(self):
        return self.name
