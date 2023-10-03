import requests
import os
import json
import time
import datetime


# Rate limit is 10 requests per minute

YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

apiKey = "5517854a8dafc7a7ebe191af41fb7c89f9f60b4f"

def get_all_contests():
    apiLink = "https://clist.by/api/v1/contest/?username=kreet&api_key=5517854a8dafc7a7ebe191af41fb7c89f9f60b4f"
    try:
        response = requests.get(apiLink)
        response.raise_for_status()

        contests = response.json()
        return contests
    except requests.exceptions.RequestException as e:
        print(RED+"[+] Failed to fetch."+RESET)
        print(">> Reason: "+str(e))
        return None

responseFolder = r"C:\Users\KREET ROUT\Desktop\cpNotifier\ResponcesRecorded"

if not os.path.exists(responseFolder):
    os.makedirs(responseFolder)
todaysDate = datetime.date.today().strftime(r"%d-%m-%Y")
fileName = f"clist_by{todaysDate}.json"
storageAddress = os.path.join(responseFolder,fileName)

while(True):
    waitTime = 86400  # refresh everyday
    print(GREEN + "[+] Requesting clist server for data" + RESET)
    jsonData = get_all_contests()
    print(GREEN+"[+] Recieved data from server."+RESET)
    print(jsonData)
    storage=open(storageAddress,'a')
    print(GREEN+f"[+] Opened file {storageAddress} in append mode."+ RESET)
    json.dump(jsonData,storage,indent = 4)
    print(GREEN+f"[+] Completed writing data to {storageAddress}."+RESET)
    print(YELLOW+ f">> Next update after {waitTime} seconds."+RESET)
    time.sleep(waitTime)
    storage.close()
