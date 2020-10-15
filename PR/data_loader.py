import json
from time import sleep

import concurrent.futures
import requests


class File_manager:
    def __init__(self):
        self.files = []


def access_url(k, ending, token, file_manager, executor):  # The method that retrieves the data to be saved in a file
    # accessing server
    url = 'http://127.0.0.1:5000'
    response = requests.get(url + ending, headers={'X-Access-Token': token})
    text = json.loads(response.text)  # extract info

    # if there are another routes we need to access them
    if 'link' in text:
        links = json.loads(response.text)['link']
        for link in links:
            executor.submit(access_url, link, links[link], token, file_manager, executor)

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
        file_manager.files.append(path)


def get_data():  # This method is used to retrieve the data from the server to our server
    fm = File_manager()  # this object will store the file list, to avoid to make files global variable
    response1 = requests.get('http://127.0.0.1:5000/register')
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=6)
    executor.submit(access_url,                                     # function that needs to be executed
                    'home',                                         # name of the file if the route will have data
                    '/home',                                        # name of the route
                    json.loads(response1.text)['access_token'],     # providing token for access
                    fm,                                             # the object where we can store files
                    executor)                                       # the function needs also to call this executor
    call_out = 20
    sleep(call_out)
    return fm.files
