from app import db


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    trade_type = db.Column(db.Integer, db.ForeignKey('TradeType.id'))
    category = db.Column(db.Integer, db.ForeignKey('Category.id'))
    created_by = db.Column(db.Integer, db.ForeignKey('Users.id'))
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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name
