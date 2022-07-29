import http.client
import json

# UNIVERSAL GET REQ
def getReq(host,url):
    try:
        connection = http.client.HTTPSConnection(host)
        connection.request("GET", url)
        res = connection.getresponse()
        data = res.read().decode()

        # return PY object in list (list of users e.g.)
        return json.loads(data)
    except:
        return None



def getUSersId():
    host = "jsonplaceholder.typicode.com"
    url = "/users"
    data = getReq(host,url)
    if data != None:
        # return arary of id's
        return [ x['id'] for x in data]
    else:
        return None


# CREATE / DELETE / UPDATE API
# https://jsonplaceholder.typicode.com/guide/ -> update / create / delete API..
def createAPI(payload):
    try:
        header = {
        'Content-type': 'application/json; charset=UTF-8',
        }
        # body = payload
        
        host = "jsonplaceholder.typicode.com"
        url = "/posts"
        
        connection = http.client.HTTPSConnection(host)
        connection.request("POST",url,json.dumps(payload),header)
        res = connection.getresponse()
        #print(res.read().decode())
        return True
    except:
        return False

def updateAPI(payload):
    try:
        header = {
        'Content-type': 'application/json; charset=UTF-8',
        }
        # body = payload
        
        host = "jsonplaceholder.typicode.com"
        url = "/posts/"+str(payload['id'])
        
        connection = http.client.HTTPSConnection(host)
        connection.request("PUT",url,json.dumps(payload),header)
        res = connection.getresponse()
        #print(res.read().decode())
        return True
    except:
        return False

def deleteAPI(post_id):
    try:      
        host = "jsonplaceholder.typicode.com"
        url = "/posts/"+str(post_id)
        
        connection = http.client.HTTPSConnection(host)
        connection.request("DELETE",url)
        return True
    except:
        return False

# payload = {
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1,
#     }
# 
# payload_for_update = {
#     'id': 1,
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1,
#   }
# 
# post_id = 1
############
# TO TEST:
############


#print(createAPI(payload))
#print(updateAPI(payload_for_update))
#print(deleteAPI(post_id))

