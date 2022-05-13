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
            userResponse=response["result"][0]
            name=""
            if "firstName" in userResponse:
                name=userResponse["firstName"]
                if "lastName" in userResponse:
                    name+=" "+userResponse["lastName"]
            userDetails["userDetails"] = {
                "handle": userResponse["handle"],
                "name": name if name else None,
                "titlePhoto": userResponse["titlePhoto"],
                "organization": userResponse["organization"] if userResponse["organization"] else None,
                "rank": userResponse["rank"],
                "rating": userResponse["rating"],
                "maxRank": userResponse["maxRank"],
                "maxRating": userResponse["maxRating"],
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