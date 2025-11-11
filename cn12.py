import socket

def dns_lookup():
    print("DNS Lookup Program")
    print("-------------------")
    user_input = input("Enter a domain name or IP address: ")

    try:
        # Check if the input is an IP address
        socket.inet_aton(user_input)  # validate IP format
        # Reverse lookup: IP → Domain
        host_name = socket.gethostbyaddr(user_input)[0]
        print(f"Domain name for IP address {user_input} is: {host_name}")

    except socket.error:
        try:
            # Forward lookup: Domain → IP
            ip_address = socket.gethostbyname(user_input)
            print(f"IP address for domain {user_input} is: {ip_address}")
        except socket.gaierror:
            print("Invalid input or unable to resolve the address.")

if __name__ == "__main__":
    dns_lookup()
