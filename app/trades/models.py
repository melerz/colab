from app import db


class Trade(db.Model):
    __tablename__= "Trade"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    trade_type = db.Column(db.Integer, db.ForeignKey('TradeType.id'))
    category = db.Column(db.Integer, db.ForeignKey('Category.id'))
    created_by = db.Column(db.Integer, db.ForeignKey('User.id'))
    is_completed = db.Column(db.Integer)  # bool

    def __repr__(self):
        return self.category

    def __init__(self, description, trade_type, category, created_by, is_completed):
        self.description = description
        self.trade_type = trade_type
        self.category = category
        self.created_by = created_by
        self.is_completed = is_completed


class TradeType(db.Model):
    __tablename__ = "TradeType"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    trades = db.relationship('Trade',backref='trade_type',lazy='dynamic')

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name


class Category(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    users = db.relationship('CategoryRelationships', backref='category', lazy='dynamic')
    trades = db.relationship('Trade',backref='category',lazy='dynamic')

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name
