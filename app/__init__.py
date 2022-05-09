# Related third party imports
from flask import Flask

app = Flask(__name__)

from app.utils.app_functions import (
    before_request,
    after_request,
)