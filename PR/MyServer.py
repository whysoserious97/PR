import socket
import sys
import traceback
import DataHandler
import json

# Server Setup
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

#Data Loading
files=DataHandler.loadData()

#Listening
s.listen(5)

while True:
    clientsocket, address = s.accept()
    while True:
        data=None
        try:
            data = clientsocket.recv(1024)
            data=data.decode('utf-8')
            if data:
                response =DataHandler.getDatabase(data,files)
                msg=json.dumps(response).encode()
                try:
                    clientsocket.sendall(msg)
                except:
                    pass
        except Exception:
            clientsocket.close()
            break
