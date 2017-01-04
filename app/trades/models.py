from app import db

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    tradeType = db.Column(db.String, db.ForeignKey('TradeType.id'))
    category = db.Column(db.String, db.ForeignKey('Category.id'))
    createdBy = db.Column(db.String, db.ForeignKey('Users.id'))
    isCompleted = db.Column(db.Integer)  # bool

    def __repr__(self):
        return self.category

class TradeType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __repr__(self):
        return self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __repr__(self):
        return self.name