import json
import random
import threading
import requests
global nr
nr=0
threadLock=threading.Lock()
def accessURL(k,ending,token):
    rs = requests.get(url + ending, headers={'X-Access-Token': token})
    if rs.status_code==200:
        text=json.loads(rs.text)
        print(k,rs.text)
        if 'link' in text:
            dict=json.loads(rs.text)['link']
            for key in dict:
                t=threading.Thread(target=accessURL,args=(key,dict[key],token))
                t.start()
        if 'data' in text:
            extension = '.json'
            if 'mime_type' in text:
                if text['mime_type']=='text/csv':
                    extension='.csv'
                elif text['mime_type']=='application/xml':
                    extension='.xml'
                elif text['mime_type']=='application/x-yaml':
                    extension='.yml'
            f=open("File_"+k+extension,"w")
            f.write(text['data'])
            f.close()
url = 'http://127.0.0.1:5000'
register = url + '/register'
response1 = requests.get(register)
if response1.status_code == 200:
    print('Success')
    print(response1.text)
    home ='/home'

    token = json.loads(response1.text) ['access_token']
    accessURL('home',home,token)
else:
    print(response1.status_code)
