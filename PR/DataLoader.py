import json
import random
import threading
from time import sleep

import requests
import concurrent.futures

queue=[]
executor=concurrent.futures.ThreadPoolExecutor(max_workers=7)
# The method that retrives the data to be saved in a file
def accessURL(k, ending, token):
    #accessing server
    url = 'http://127.0.0.1:5000'
    rs = requests.get(url + ending, headers={'X-Access-Token': token})

    #getting response
    if rs.status_code == 200:
        text = json.loads(rs.text)     #extract info
        print(k, rs.text)

        # if there are another routes we need to access them
        if 'link' in text:
            dict = json.loads(rs.text) ['link']
            for key in dict:
                insidefuture = executor.submit(accessURL,key, dict [key], token )
                queue.append(insidefuture)

        #by default is JSON, but if there is mentioned an extension we need to parse it differently
        extension = '.json'
        if 'mime_type' in text:
            if text ['mime_type'] == 'text/csv':
                extension = '.csv'
            elif text ['mime_type'] == 'application/xml':
                extension = '.xml'
            elif text ['mime_type'] == 'application/x-yaml':
                extension = '.yml'

        #Then we are saving this data in a file
        if 'data' in text:
            path = "File_" + k + extension
            f = open(path, "w")
            f.write(text ['data'])
            f.close()
            files.append(path)

#This method is used to retrive the data from the server to our server
def getData():
    response1 = requests.get('http://127.0.0.1:5000/register')
    if response1.status_code == 200:
        print('Success')
        print(response1.text)
        home ='/home'
        token = json.loads(response1.text) ['access_token']
        future=executor.submit(accessURL,'home',home,token)
        queue.append(future)
        #accessURL('home',home,token)
        callout=20
        sleep(callout)
        return files

    print(response1.status_code)
    return []

threads=[]
files=[]
