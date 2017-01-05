from app import db


class Trade(db.Model):
    __tablename__= "Trade"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    trade_type = db.Column(db.Integer, db.ForeignKey('TradeType.id'))
    category = db.Column(db.Integer, db.ForeignKey('Category.id'))
    created_by = db.Column(db.Integer, db.ForeignKey('User.id'))
    is_completed = db.Column(db.Integer)  # bool

    def __repr__(self):
        return self.description

    def __init__(self, description, trade_type, category, created_by, is_completed=0):
        self.description = description
        self.trade_type = trade_type
        self.category = category
        self.created_by = created_by
        self.is_completed = is_completed


class TradeType(db.Model):
    __tablename__ = "TradeType"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    trades = db.relationship('Trade', backref='my_trade_type', lazy='dynamic')

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name


class Category(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    users = db.relationship('CategoryRelationships', backref='all_category', lazy='dynamic')
    trades = db.relationship('Trade', backref='my_category', lazy='dynamic')

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name
