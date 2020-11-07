import socket
from UDP_protocol import *
msgFromClient = "Hello UDP Server"


serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
bytesToSend = str.encode('Connect')
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
print('Me as client I have sent:',bytesToSend)
# Send to server using created UDP socket


send_msg(UDPClientSocket,msgFromClient,serverAddressPort)

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msgFromServer= recieve_msg(UDPClientSocket,bufferSize,serverAddressPort)

msg = "Server: {}".format(msgFromServer)

print(msg)

send_msg(UDPClientSocket,'Hello Again Server',serverAddressPort)
msgFromServer= recieve_msg(UDPClientSocket,bufferSize,serverAddressPort)
print(msgFromServer)