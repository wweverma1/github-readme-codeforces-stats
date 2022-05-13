# Related third party imports
from flask import (
    jsonify,
    request,
    send_file,
)

from app.stats.models import (
    User,
)

from app.utils.card.card import (
    Card
)

# for creating a pie chart
# import matplotlib.pyplot as plt
# import numpy as np


def fetch_stats():
    username = request.args.get('username', type=str)
    theme_id = request.args.get('theme', type=int, default=1)
    user_details = User.fetch_user_details(username)
    if user_details["status"]=="OK":
        submission_details = User.fetch_submission_details(username)
        # creating a pie chart
            # y = np.array([submission_details["ac"], submission_details["tle"], submission_details["wa"], submission_details["others"]])
            # mylabels = ["Accepted", "Time Limited Exceeeded", "Wrong Answer", "Others"]
            # plt.pie(y, labels = mylabels)
            # plt.show()
        Card.generate_stats_card(user_details["userDetails"], submission_details, theme_id)
        return send_file('./../card.svg', mimetype='image/svg+xml'), 200
    else:
        comment=user_details["comment"]
    return jsonify({"status": "FAILED", "comment": comment}), 400
    