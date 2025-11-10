# client_hello.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))

# Send message
client_socket.send("Hello from Client!".encode())

# Receive reply
data = client_socket.recv(1024).decode()
print("Server says:", data)

client_socket.close()
