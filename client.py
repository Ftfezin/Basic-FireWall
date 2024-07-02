import socket

server_ip = "SERVER IP"
server_port =  5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

response = client_socket.recv(1024)
print("Response from server:", response.decode())

client_socket.close()