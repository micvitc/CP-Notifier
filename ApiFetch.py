import requests
import os
import json
import time
import datetime
from flask import Flask,jsonify


# Rate limit is 10 requests per minute

YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

app = Flask(__name__)

@app.route("/")
def mainPage():
    return "CP Notifier"

@app.route('/clist.by')
def clistby():
    apiKey = "5517854a8dafc7a7ebe191af41fb7c89f9f60b4f"
    apiLink = "https://clist.by/api/v1/contest/?username=kreet&api_key=5517854a8dafc7a7ebe191af41fb7c89f9f60b4f"
    try:
        response = requests.get(apiLink)
        response.raise_for_status()
        contests = response.json()
        responseFolder = r"C:\Users\KREET ROUT\Desktop\cpNotifier\ResponcesRecorded"
        if not os.path.exists(responseFolder):
            os.makedirs(responseFolder)
        fileName = f"events.json"
        storageAddress = os.path.join(responseFolder,fileName)
        with open("ResponcesRecorded/events.json","a") as jsonFile:
            json.dump(contests,jsonFile)
        return jsonify(contests)
    except requests.exceptions.RequestException as e:
        print(RED+"[+] Failed to fetch."+RESET)
        print(">> Reason: "+str(e))
        return None


