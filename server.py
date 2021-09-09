import socket
import threading


class server_thread(threading.Thread):
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address
    
    def run(self):
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            print(data)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1",65431))
server_socket.listen()

(client_socket, address) = server_socket.accept()
print("Connected by", address)

while True:
    data = client_socket.recv(1024)
    #if not data: 
    print("Received ", data)