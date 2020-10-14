import json
from time import sleep

import concurrent.futures
import requests

queue = []
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)


def access_url(k, ending, token):  # The method that retrieves the data to be saved in a file
    # accessing server
    url = 'http://127.0.0.1:5000'
    response = requests.get(url + ending, headers={'X-Access-Token': token})

    # getting response
    if response.status_code == 200:
        text = json.loads(response.text)  # extract info
        print(k, response.text)

        # if there are another routes we need to access them
        if 'link' in text:
            my_dict = json.loads(response.text)['link']
            for key in my_dict:
                inside_future = executor.submit(access_url, key, my_dict[key], token)
                queue.append(inside_future)

        # by default is JSON, but if there is mentioned an extension we need to parse it differently
        extension = '.json'
        if 'mime_type' in text:
            if text['mime_type'] == 'text/csv':
                extension = '.csv'
            elif text['mime_type'] == 'application/xml':
                extension = '.xml'
            elif text['mime_type'] == 'application/x-yaml':
                extension = '.yml'

        # Then we are saving this data in a file
        if 'data' in text:
            path = "File_" + k + extension
            file = open(path, "w")
            file.write(text['data'])
            file.close()
            files.append(path)


def get_data():  # This method is used to retrieve the data from the server to our server
    response1 = requests.get('http://127.0.0.1:5000/register')
    if response1.status_code == 200:
        print('Success')
        print(response1.text)
        home = '/home'
        token = json.loads(response1.text)['access_token']
        future = executor.submit(access_url, 'home', home, token)
        queue.append(future)
        # accessURL('home',home,token)
        call_out = 20
        sleep(call_out)
        return files

    print(response1.status_code)
    return []


threads = []
files = []
