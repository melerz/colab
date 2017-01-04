from app import db


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    job = db.Column(db.String(50))
    team = db.Column(db.Integer, db.ForeignKey('Team.id'))
    picture = db.Column(db.String(200))
    works_on = db.Column(db.Integer, db.ForeignKey('Event.id'))
    country = db.Column(db.String(50))
    name = db.Column(db.String(50))
    password = db.Column(db.Integer)
    location = db.Column(db.Integer)  # coordinates
    #events = db.relationship('Event',backref='user',lazy='dynamic')
    #categories = db.relationship('CategoryRelationships',backref='user',lazy='dynamic')
    #trades = db.relationship('Trade',backref='user',lazy='dynamic')

    def __repr__(self):
        return self.userName

    def __init__(self, user_name, job, picture=None, works_on=None, country=None, name=None, password=None, location=None,team=None):
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
    __tablename__ = 'Team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
   # users = db.relationship('users.User',backref='team',lazy='dynamic') #todo backref may shadow

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name


class CategoryRelationships(db.Model):
    __tablename__ = "CategoryRelationship"
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.Integer, db.ForeignKey('Category.id'))
    user_name = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __init__(self, category_name, user_name):
        self.category_name = category_name
        self.user_name = user_name


