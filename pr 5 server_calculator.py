# server_calculator.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5002))
server.listen(1)

print("🔹 Calculator Server is ready...")
conn, addr = server.accept()
print("✅ Connected to:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("❌ Connection closed.")
        break
    print(f"Expression from client: {data}")
    try:
        result = str(eval(data))
    except Exception:
        result = "Error"
    conn.send(result.encode())

conn.close()
server.close()
