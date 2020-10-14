import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    query = input('Insert query:\n')
    full_msg = ''
    ##########################
    print('sending' + query)
    s.send(query.encode())
    ##########################
    isNext = True
    while isNext:
        try:
            msg = s.recv(2048)
            full_msg += msg.decode('utf-8')
            if len(msg) < 2048:
                isNext = False
        finally:
            pass

    print(full_msg)

    # SelectColumn email
    # SelectFromColumn first_name Brand
