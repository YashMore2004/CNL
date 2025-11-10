# client_file.py
import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5001))

filename = 'send_file.txt'

# Create a sample file
with open(filename, 'w') as f:
    f.write("This is a sample file sent via TCP socket.\n")

# Send file
print("📤 Sending file...")
with open(filename, 'rb') as f:
    data = f.read(1024)
    while data:
        client.send(data)
        data = f.read(1024)

print("✅ File sent successfully.")
client.close()
