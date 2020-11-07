import hashlib
import json
m = hashlib.md5()
def send_msg(skt,msg,address):
    dict={}
    dict['msg']=msg
    m.update(str.encode(msg))
    dict['cksm']=m.hexdigest()
    byte_dict=json.dumps(dict)
    bytesToSend  = str.encode(byte_dict)
    skt.sendto(bytesToSend,address)

    response = skt.recvfrom(1024)
    #print(response[0])
    if response[0] == b'ack':
        return
    else:
        i=0
        while response[0]!=b'ack' and i<4:
            i+=1
            skt.sendto(bytesToSend,address)
            response = skt.recvfrom(1024)
            #print(response[0])

def recieve_msg(skt,bufferSize,address):

    body = skt.recvfrom(bufferSize)
    decoded_body = json.loads(body[0].decode())
    m.update(str.encode(decoded_body['msg']))
    a=decoded_body['cksm']  # in the body
    # print('Recieved',decoded_body['cksm'])
    b=m.hexdigest()    # after rehashing
    if a==b :
        skt.sendto(b'ack',address)
        return decoded_body['msg']
    else:
        skt.sendto(b'nack', address)