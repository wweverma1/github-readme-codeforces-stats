# Standard library imports
import time
from datetime import datetime

# Related third party imports
from flask import request

# Local app specific imports
from app import app


@app.before_request
def before_request():
    request.start_time = time.time()


@app.after_request
def after_request(response):
    if request.endpoint:
        end_time = time.time()
        latency = int((end_time - request.start_time) * 1000)
        print(f'[ {str(datetime.now())}] endpoint {request.endpoint} latency {latency}')
    return response