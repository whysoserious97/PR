import socket
import sys
import traceback

import DataHandler
import json

HEADERSIZE=10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print('clientsocket from:' + str(address))
    while True:
        data=None
        try:
            data = clientsocket.recv(1024)
            data=data.decode('utf-8')
            print('recived:' + data)
            response = DataHandler.getDatabase(data)
            if data:
                print('sending msg back to the client')
                msg=json.dumps(response).encode()
                try:
                    clientsocket.sendall(msg)
                except:
                    pass
        except Exception:
            print(traceback.print_exc(file=sys.stdout))
            print('Fail...')
            clientsocket.close()
            break
