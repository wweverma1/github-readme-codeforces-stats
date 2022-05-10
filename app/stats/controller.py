# Related third party imports
import json
import requests
from flask import (
    jsonify,
    request,
)


def fetch_stats():
    username = request.args.get('u', type=str)
    theme_id = request.args.get('t', type=int, default=1)
    payload = {'handles': username}
    cfResponse = requests.get('https://codeforces.com/api/user.info', params=payload)
    if cfResponse.status_code==200:
        status="OK"
        cfResponse=cfResponse.json()
        result = {
            "handle": cfResponse["result"][0]["handle"],
            "titlePhoto": cfResponse["result"][0]["titlePhoto"],
            "organization": cfResponse["result"][0]["organization"],
            "rank": cfResponse["result"][0]["rank"],
            "rating": cfResponse["result"][0]["rating"],
            "maxRank": cfResponse["result"][0]["maxRank"],
            "maxRating": cfResponse["result"][0]["maxRating"],
            "cardTheme": "light" if theme_id==1 else "dark",
        }
        return jsonify({"status": status, "result": result}), 200
    else:
        status="FAILED"
        if cfResponse.status_code==400:
            comment=cfResponse.json()["comment"]
        else:
            comment="Internal Server Error"
    return jsonify({"status": status, "comment": comment}), 400