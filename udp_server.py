# udp_server.py
import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 6000))

print("🔹 UDP Server ready and waiting for file...")

# Receive file name
filename, addr = server_socket.recvfrom(1024)
filename = filename.decode()
print(f"📥 Receiving file: {filename}")

# Open file to write in binary mode
with open("received_" + filename, 'wb') as f:
    while True:
        data, addr = server_socket.recvfrom(1024)
        if data == b'EOF':
            break
        f.write(data)

print(f"✅ File received successfully and saved as received_{filename}")
server_socket.close()
