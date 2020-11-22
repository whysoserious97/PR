import socket
from PR_LAB_2.UDP_protocol import *
import PR_LAB_2.SRSAP as SRSAP
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 10240

class UDP_server:
    def recieve(self):
        print('UDP_server')
        return self.server_SRSAP.secure_recieve()

    def send(self,msg):
        self.server_SRSAP.secure_send(msg)
        response = self.server_SRSAP.secure_recieve()
        return response

    def __init__(self,destination):
        self.bufferSize = 10240
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocket.bind(destination)

        print("UDP server up and listening")
        self.connected, self.address = self.UDPServerSocket.recvfrom(bufferSize)
        print('Client Connected:',self.connected)

        self.client_n = base64.b64decode(recieve_msg(self.UDPServerSocket,bufferSize,self.address)).decode()
        self.client_e = base64.b64decode(recieve_msg(self.UDPServerSocket,bufferSize,self.address)).decode()
        his_key = SRSAP.create_pub_key(self.client_n, self.client_e)
        #print(client_n)
        self.keys = SRSAP.createkeys()

        send_msg(self.UDPServerSocket,base64.b64encode(str(self.keys[0].n).encode()),self.address)
        send_msg(self.UDPServerSocket,base64.b64encode(str(self.keys[0].e).encode()),self.address)



        self.server_SRSAP = SRSAP.SRSAP(self.keys[0],self.keys[1],his_key,self.UDPServerSocket,self.address)


        # while (True):
        #     message = server_SRSAP.secure_recieve()
        #     #message=recieve_msg(UDPServerSocket,1024,address)
        #
        #     clientMsg = "Client:{}".format(message)
        #     print(clientMsg)
        #     server_SRSAP.secure_send("Hello From SERVER!!!")