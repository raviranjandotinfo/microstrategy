import requests
import json
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np

### Defining parameters values ###
username = 'ravir'
password = ''
iserver = 'https://raviranjan.info'
projectId = 'mst_pro_01'
projectName = 'Fetch MicroStrategy Data & Reports'
baseURL = "https://raviranjan.info/MicroStrategyLibrary/api/"

### Login function to authenticate and match credentials ###
def login(baseURL,username,password):
    header = {'username': username,
                'password': password,
                'loginMode': 1}
    r = requests.post(baseURL + 'auth/login', data=header)
    if r.ok:
        authToken = r.headers['X-MSTR-AuthToken']
        cookies = dict(r.cookies)
        print("Token: " + authToken)
        print("Session ID: {}".format(cookies))
        return authToken, cookies
    else:
        print("HTTP {} - {}, Message {}".format(r.status_code, r.reason, r.text))
        return []
      
### Calling above function ###
  authToken, cookies = login(baseURL,username,password)
# output would be  {Token: tokenId-01, Session ID: {'Session-Name-01': 'Session-Id-nm-01'}}
