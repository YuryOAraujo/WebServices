import socket

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = client_socket.recv(1024)
print(message.decode('utf-8'))

client_socket.close()
