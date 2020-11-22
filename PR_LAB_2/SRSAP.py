'''
SRSAP - Secure RSA Protocol )
'''
import rsa
import PR_LAB_2.UDP_protocol as UDP_protocol
import base64
import json
import pickle


def create_pub_key(n,e):
    return rsa.PublicKey(int(n),int(e))

def createkeys():
    (my_pub, my_priv) = rsa.newkeys(800)
    return (my_pub,my_priv)

class SRSAP:
    def __init__(self,my_pub,my_priv,his_pub_key,skt,address):
        self.his_pub_key=his_pub_key
        self.my_pub=my_pub
        self.my_priv=my_priv
        self.skt=skt
        self.address=address

    def secure_send(self,msg):
        message=msg.encode('utf8')
        crypto = rsa.encrypt(message, self.his_pub_key)
        UDP_protocol.send_msg(self.skt,base64.b64encode(crypto),self.address)

    def secure_recieve(self):
        print('Entered')
        crypto=base64.b64decode(UDP_protocol.recieve_msg(self.skt,10240,self.address))
        print('exit')
        msg = rsa.decrypt(crypto, self.my_priv)
        message=msg.decode()
        return message
