import socket
from UDP_protocol import *

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
message,address = UDPServerSocket.recvfrom(bufferSize)
print('The client sent:',message)
bytesToSend = str.encode('Confirmed connection')
UDPServerSocket.sendto(bytesToSend, address)
while (True):
    message=recieve_msg(UDPServerSocket,1024,address)

    clientMsg = "Client:{}".format(message)
    print(clientMsg)
    send_msg(UDPServerSocket,"Hello from server",address)