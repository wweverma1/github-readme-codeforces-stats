from flask import Blueprint

from app.home.controller import (
    home
)

home_api = Blueprint('home', __name__)

home_api.add_url_rule(rule='/', view_func=home, methods=['GET', ])
