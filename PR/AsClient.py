import socket

#query="SelectColumn email"
#query='SelectFromColumn first_name ^R.*'
query=input('Insert query:\n')
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
while True:
    full_msg= ''
    ##########################
    print('sending'+query)
    s.send(query.encode())
    ##########################
    isNext=True
    while isNext:
            try:
                msg=s.recv(8)
                full_msg += msg.decode('utf-8')
                if len(msg)<8:
                    isNext=False
            finally:
                pass
    print(full_msg)
    query=input('Insert query:\n')