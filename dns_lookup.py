# dns_lookup.py
import socket

print("=== DNS Lookup Program ===")
print("1. URL to IP address")
print("2. IP address to URL")

choice = input("Enter your choice (1 or 2): ")

try:
    if choice == '1':
        # Domain name to IP address
        domain = input("Enter domain name (e.g., www.google.com): ")
        ip = socket.gethostbyname(domain)
        print(f"🌐 IP address of {domain} is: {ip}")

    elif choice == '2':
        # IP address to domain name
        ip = input("Enter IP address (e.g., 142.250.183.4): ")
        domain = socket.gethostbyaddr(ip)
        print(f"🔗 Domain name for {ip} is: {domain[0]}")

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

except socket.gaierror:
    print("⚠️ DNS Lookup failed. Invalid domain or IP address.")
except Exception as e:
    print("❌ Error:", e)
