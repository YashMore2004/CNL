import ipaddress

# Function to find IP class
def find_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Invalid IP"

# Function to demonstrate subnetting
def demonstrate_subnetting(ip_with_prefix):
    try:
        network = ipaddress.ip_network(ip_with_prefix, strict=False)
        
        print("--------------------------------------------------")
        print(f"Input Network: {ip_with_prefix}")
        print(f"IP Class: {find_ip_class(str(network.network_address))}")
        print("--------------------------------------------------")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Total Subnets: {2 ** (network.prefixlen - network.max_prefixlen)}")
        print(f"Total Hosts per Subnet: {network.num_addresses - 2}")
        print("--------------------------------------------------")

        # Display all possible subnets (for example purpose, limit to first 5)
        print("First few possible subnets:")
        subnets = list(network.subnets(new_prefix=network.prefixlen + 2))  # Example: 4 subnets
        for i, subnet in enumerate(subnets[:5]):
            print(f"Subnet {i+1}: {subnet}")

    except Exception as e:
        print("Error:", e)

# Example execution
if __name__ == "__main__":
    ip_with_prefix = input("Enter an IP network (e.g. 192.168.1.0/24): ")
    demonstrate_subnetting(ip_with_prefix)
