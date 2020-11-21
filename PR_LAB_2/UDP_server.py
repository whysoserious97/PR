import socket
from UDP_protocol import *
import SRSAP
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
connected, address = UDPServerSocket.recvfrom(bufferSize)
print('Client Connected:',connected)

client_n = base64.b64decode(recieve_msg(UDPServerSocket,bufferSize,address)).decode()
client_e = base64.b64decode(recieve_msg(UDPServerSocket,bufferSize,address)).decode()
his_key = SRSAP.create_pub_key(client_n, client_e)
print(client_n)
keys = SRSAP.createkeys()

send_msg(UDPServerSocket,base64.b64encode(str(keys[0].n).encode()),address)
send_msg(UDPServerSocket,base64.b64encode(str(keys[0].e).encode()),address)



server_SRSAP = SRSAP.SRSAP(keys[0],keys[1],his_key,UDPServerSocket,address)
while (True):
    message = server_SRSAP.secure_recieve()
    #message=recieve_msg(UDPServerSocket,1024,address)

    clientMsg = "Client:{}".format(message)
    print(clientMsg)
    server_SRSAP.secure_send("Hello From SERVER!!!")