### Creating sessionValiade function to validate the previously created session via login.py ###
def sessionValiade(baseURL, authToken, cookies):
    print("Checking session...")
    header = {'X-MSTR-AuthToken': authToken,
                 'Accept': 'application/json'}
    r = requests.get(baseURL + "sessions", headers=header, cookies=cookies)
    
    if r.ok:
        print(r.text)
    else:
        print("HTTP {} - {}, Message {}".format(r.status_code, r.reason, r.text))
        return []

### Calling function to run in this file ###
sessionValiade(baseURL, authToken, cookies)

# output : {"locale":lclId,"maxSearch":configuredmxseNo,"workingSet":10,"timeout":600,"id":"IdNo","fullName":"ravi","initials":"r"}
