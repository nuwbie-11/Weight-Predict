from flask import Blueprint
from controllers.homes import *


user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(home)
user_bp.route('/about', methods=['GET'])(about)
