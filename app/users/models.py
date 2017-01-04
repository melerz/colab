from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    job = db.Column(db.String(50))
    team = db.Column(db.Integer, db.ForgeinKey('Team.id'))
    picture = db.Column(db.String(200))
    works_on = db.Column(db.Integer, db.ForgeinKey('Event.id'))
    country = db.Column(db.String(50))
    name = db.Column(db.String(50))
    password = db.Column(db.Integer)
    location = db.Column(db.Integer)  # coordinates

    def __repr__(self):
        return self.userName

    def __init__(self, user_name, job, team, picture, works_on, country, name, password, location):
        self.user_name = user_name
        self.job = job
        self.team = team
        self.picture = picture
        self.works_on = works_on
        self.country = country
        self.name = name
        self.password = password
        self.location = location


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name


class CategoryRelationships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.Integer, db.ForgeinKey('Category.id'))
    user_name = db.Column(db.Integer, db.ForgeinKey('User.id'))

    def __init__(self, category_name, user_name):
        self.category_name = category_name
        self.user_name = user_name

