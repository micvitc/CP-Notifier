import requests
import os
import json
import time
import datetime
from flask import Flask,jsonify


# Rate limit is 10 requests per minute

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
        return jsonify(contests)
    except requests.exceptions.RequestException as e:
        print(RED+"[+] Failed to fetch."+RESET)
        print(">> Reason: "+str(e))
        return None


