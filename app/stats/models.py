# Related third party imports
import json
import requests


class User:

    def fetch_user_details(username):
        userDetails = {}
        payload = {'handles': username}
        response = requests.get('https://codeforces.com/api/user.info', params=payload)
        if response.status_code==200:
            userDetails["status"] = "OK"
            response=response.json()
            userDetails["userDetails"] = {
                "handle": response["result"][0]["handle"],
                "titlePhoto": response["result"][0]["titlePhoto"],
                "organization": response["result"][0]["organization"],
                "rank": response["result"][0]["rank"],
                "rating": response["result"][0]["rating"],
                "maxRank": response["result"][0]["maxRank"],
                "maxRating": response["result"][0]["maxRating"],
            }
        else:
            userDetails["status"] = "FAILED"
            if response.status_code==400:
                comment=response.json()["comment"]
            else:
                comment="Internal Server Error"
            userDetails["comment"] = comment
        return userDetails

    def fetch_submission_details(username):
        payload = {'handle': username}
        response = requests.get('https://codeforces.com/api/user.status', params=payload)
        if response.status_code==200:
            submissionDetails = {}
            response=response.json()
            ac=0
            wa=0
            tle=0
            others=0
            total=len(response["result"])
            for submission in response["result"]:
                if submission["verdict"]=="OK":
                    ac+=1
                elif submission["verdict"]=="TIME_LIMIT_EXCEEDED":
                    tle+=1
                elif submission["verdict"]=="WRONG_ANSWER":
                    wa+=1
                else:
                    others+=1
            submissionDetails = {
                "total": total,
                "ac": ac,
                "wa": wa,
                "tle": tle,
                "others": others,
            }
            return submissionDetails
        else:
            print("Error in codeforces API")
            return None