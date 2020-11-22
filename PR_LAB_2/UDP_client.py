import socket
from PR_LAB_2.UDP_protocol import *
import PR_LAB_2.SRSAP as SRSAP
msgFromClient = "Hello UDP Server"
import json

# serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 10240

# Create a UDP socket at client side

class UDP_client:
    def send(self,msg):
        self.client_SRSAP.secure_send(msg)
        response = self.client_SRSAP.secure_recieve()
        return response

    def __init__(self,serverAddressPort):
        self.serverAddressPort = serverAddressPort
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.keys=SRSAP.createkeys()
        self.bytesToSend='Client_A'.encode()
        self.UDPClientSocket.sendto(self.bytesToSend, serverAddressPort)

        send_msg(self.UDPClientSocket,base64.b64encode(str(self.keys[0].n).encode()),serverAddressPort)
        send_msg(self.UDPClientSocket,base64.b64encode(str(self.keys[0].e).encode()),serverAddressPort)

        self.server_n=base64.b64decode(recieve_msg(self.UDPClientSocket,bufferSize,self.serverAddressPort)).decode()
        self.server_e=base64.b64decode(recieve_msg(self.UDPClientSocket,bufferSize,self.serverAddressPort)).decode()

        self.server_key=SRSAP.create_pub_key(self.server_n,self.server_e)

        # Send to server using created UDP socket

        self.client_SRSAP = SRSAP.SRSAP(self.keys[0],self.keys[1],self.server_key,self.UDPClientSocket,serverAddressPort)

        # client_SRSAP.secure_send("Hello Server")

        # response=client_SRSAP.secure_recieve()
        # print(response)
