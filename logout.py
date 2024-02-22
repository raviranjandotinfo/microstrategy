### creating logout function to successfully end the session ###
def logout(baseURL,authToken):
    
    header = {'X-MSTR-AuthToken': authToken,
                  'Accept': 'application/json'}

    r = requests.post(baseURL + 'auth/logout',headers=header, cookies=cookies)
    if r.ok:
        print("Logged Out")
       
    else:
        print("HTTP {} - {}, Message {}".format(r.status_code, r.reason, r.text))

### calling logout to end the session ###
logout(baseURL, authToken)
# output : Successfully logout
