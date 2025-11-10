# server_file.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5001))
server.listen(1)

print("🔹 Waiting for connection...")
conn, addr = server.accept()
print("✅ Connected to:", addr)

filename = 'received_file.txt'
with open(filename, 'wb') as f:
    print("📥 Receiving file...")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print(f"✅ File saved as {filename}")
conn.close()
server.close()
