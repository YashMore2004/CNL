# udp_client.py
import socket
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = '127.0.0.1'
server_port = 6000

# Choose any file to send
filename = input("Enter file name to send (with extension): ")

if not os.path.exists(filename):
    print("❌ File not found!")
    exit()

# Send file name first
client_socket.sendto(filename.encode(), (server_ip, server_port))

# Send file content
with open(filename, 'rb') as f:
    data = f.read(1024)
    while data:
        client_socket.sendto(data, (server_ip, server_port))
        data = f.read(1024)

# Send End Of File message
client_socket.sendto(b'EOF', (server_ip, server_port))

print(f"✅ File '{filename}' sent successfully!")
client_socket.close()
