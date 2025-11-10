# server_hello.py
import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(1)

print("🔹 Server is waiting for connection...")
conn, addr = server_socket.accept()
print("✅ Connected to:", addr)

# Receive message from client
data = conn.recv(1024).decode()
print("Client says:", data)

# Send response
conn.send("Hello from Server!".encode())

conn.close()
server_socket.close()
