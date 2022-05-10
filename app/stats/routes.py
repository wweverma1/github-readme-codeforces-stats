from flask import Blueprint

from app.stats.controller import (
    fetch_stats,
)

stats_api = Blueprint('stats', __name__)

stats_api.add_url_rule(rule='/stats', view_func=fetch_stats, methods=['GET', ])