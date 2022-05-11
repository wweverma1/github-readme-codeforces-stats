# Related third party imports
from flask import (
    jsonify,
    request,
)

from app.stats.models import (
    User,
)


def fetch_stats():
    username = request.args.get('u', type=str)
    theme_id = request.args.get('t', type=int, default=1)
    user_details = User.fetch_user_details(username)
    if user_details["status"]=="OK":
        submission_details = User.fetch_submission_details(username)
        return jsonify({"status": "OK", "userDetails": user_details["userDetails"], "submissionDetails": submission_details}), 200
    else:
        comment=user_details["comment"]
    return jsonify({"status": "FAILED", "comment": comment}), 400
    