import socket
import json
from PR_LAB_2.UDP_client import UDP_client
from PR_LAB_2.UDP_server import UDP_server


class App_Protocol():
    method = None
    parameters = None
    bufferSize = 10240
    controler = None
    def __init__(self,destination,type):
        if type == 'server':
            self.controler = UDP_server(destination)
        elif type == 'client':
            self.controler = UDP_client(destination)

    def send(self):
        body={}
        body['method'] = self.method
        body['parameters'] = self.parameters
        msg = json.dumps(body)
        response = self.controler.send(msg)
        response = json.loads(response)
        return response
        # message = response['parameters']
        # return message
    def recieve(self):
        return self.controler.recieve()

    def isValid(self,card_info):
        if card_info == '123 321':
            return 'Success'
        else:
            return 'Invalid'
