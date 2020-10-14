import socket
import data_handler
import json
from threading import Thread


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):

        while True:
            data = conn.recv(2048)
            data = data.decode('utf-8')
            if data:
                response = data_handler.get_database(data, files)
                msg = json.dumps(response).encode()
                # try here

                conn.sendall(msg)


# Server Setup
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((socket.gethostname(), 1234))
threads = []

# Data Loading
files = data_handler.load_data()

# Listening
tcpServer.listen(5)

while True:
    tcpServer.listen(5)
    conn, (the_ip, the_port) = tcpServer.accept()
    new_thread = ClientThread(the_ip, the_port)
    new_thread.start()
    threads.append(new_thread)
