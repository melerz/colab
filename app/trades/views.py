# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify
from flask_restful import Resource, Api, fields, marshal_with
from app.trades.models import *

trades = Blueprint('trades', __name__)
api = Api()
api.init_app(trades)

trade_json = {
    'id': fields.Integer,
    'description': fields.String,
    'trade_type': fields.String,
    'category': fields.String,
    'created_by': fields.String,
    'is_completed': fields.String
}


class Trades(Resource):
    @marshal_with(trade_json)
    def get(self, trade_id=None):
        if trade_id:
            events = Trade.query.filter(Trade.id == trade_id).all()
        else:
            events = Trade.query.all()
        return events

    def post(self):
        data = request.get_json()
        new_trade = Trade(data['description'], data['trade_type'], data['category'], data['created_by'])
        db.session.add(new_trade)
        db.session.commit()
        return {"result": "success"}, 201

    def delete(self, trade_id):
        my_trade = Trade.query.filter(Trade.id == trade_id).first()
        my_trade.is_completed = 1
        db.session.add(my_trade)
        db.session.commit()


class TradeTypeRelationshipView(Resource):
    @marshal_with(trade_json)
    def get_all_trades_by_type(self, type_id):
        all_trades = TradeType.get(type_id)
        return all_trades.trades.all()


class TradeCategoryRelationshipView(Resource):
    @marshal_with(trade_json)
    def get_all_trades_by_category(self, cat_type_id):
        all_trades = Category.get(cat_type_id)
        return all_trades.trades.all()


user_json = {
    'id': fields.String,
    'user_name': fields.String,
    'job': fields.String,
    'picture': fields.String,
    'works_on': fields.String,
    'country:': fields.String,
    'name': fields.String,
    'password': fields.String,
    'location': fields.Integer,
    'team': fields.String

}


class UserCategoryRelationshipView(Resource):
    @marshal_with(user_json)
    def get_all_users_by_category(self, cat_id):
        all_users = Category.get(cat_id)
        return all_users.users.all()


trade_type_json = {
    "id": fields.Integer,
    "name": fields.String
}


class TradeTypeView(Resource):
    @marshal_with(trade_type_json)
    def get(self, trade_type_id=None):
        if trade_type_id:
            trade_types = TradeType.query.filter(Trade.id == trade_type_json).all()
        else:
            trade_types = TradeType.query.all()
        return trade_types

    def post(self):
        pass

    def delete(self):
        pass


category_json = {
    "id": fields.Integer,
    "name": fields.String
}


class CategoryView(Resource):
    @marshal_with(category_json)
    def get(self, cat_id=None):
        if cat_id:
            categories = Category.query.filter(Trade.id == cat_id).all()
        else:
            categories = Category.query.all()
        return categories

    def post(self):
        pass

    def delete(self, cat_id):
        pass


api.add_resource(Trades, '/', '/<int:trade_id>')
api.add_resource(TradeTypeView, '/', '/<int:trade_type_id>')
api.add_resource(TradeTypeRelationshipView, '/<int:type_id>')
api.add_resource(CategoryView, '/category', '/<int:cat_id>')
api.add_resource(TradeCategoryRelationshipView, '/<int:cat_type_id>')
api.add_resource(UserCategoryRelationshipView, '/<int:cat_id>')
