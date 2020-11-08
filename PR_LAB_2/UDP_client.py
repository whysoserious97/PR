import socket
from UDP_protocol import *
import SRSAP
msgFromClient = "Hello UDP Server"
import json

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

keys=SRSAP.createkeys()
print(keys[0].n)
bytesToSend='Client_A'.encode()
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

send_msg(UDPClientSocket,base64.b64encode(str(keys[0].n).encode()),serverAddressPort)
send_msg(UDPClientSocket,base64.b64encode(str(keys[0].e).encode()),serverAddressPort)

# UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# server_n=recieve_msg(UDPClientSocket,bufferSize,serverAddressPort)
# server_e=recieve_msg(UDPClientSocket,bufferSize,serverAddressPort)

server_n=base64.b64decode(recieve_msg(UDPClientSocket,bufferSize,serverAddressPort)).decode()
server_e=base64.b64decode(recieve_msg(UDPClientSocket,bufferSize,serverAddressPort)).decode()

server_key=SRSAP.create_pub_key(server_n,server_e)

# Send to server using created UDP socket

client_SRSAP = SRSAP.SRSAP(keys[0],keys[1],server_key,UDPClientSocket,serverAddressPort)

client_SRSAP.secure_send("Hello Server")

response=client_SRSAP.secure_recieve()
print(response)

client_SRSAP.secure_send("Hello Again Server")
response=client_SRSAP.secure_recieve()
print(response)
