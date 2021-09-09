import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1",65431))
server_socket.listen()

(client_socket, address) = server_socket.accept()
print("Connected by", address)

while True:
    data = client_socket.recv(1024)
    #if not data: 
    print("Received ", data)