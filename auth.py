### Getting users info from from previously validated sessions ###
def userInfo(baseURL, authToken, cookies):
    header = {'X-MSTR-AuthToken': authToken,
                 'Accept': 'application/json'}
    r = requests.get(baseURL + "sessions/userInfo", headers=header, cookies=cookies)
    
    if r.ok:
        return json_normalize(json.loads(r.text))
    else:
        print("HTTP {} - {}, Message {}".format(r.status_code, r.reason, r.text))
        return []

### Calling userInfo function to get the info ###
user = userInfo(baseURL, authToken, cookies)

# Sample output : {fullName:ravi, id:idNo,	initials:r, metadataUser:Truse} in tabular format. 
