# client_calculator.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5002))

print("✅ Connected to Calculator Server.")
print("Type expressions (e.g. 5+6*2) or 'exit' to quit.\n")

while True:
    expr = input("Enter expression: ")
    client.send(expr.encode())
    if expr.lower() == 'exit':
        break
    data = client.recv(1024).decode()
    print("Result from server:", data)

client.close()
