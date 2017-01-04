from flask import Blueprint


users = Blueprint('users', __name__,url_prefix='/users')


@users.route('/')
def index():
    return "users"