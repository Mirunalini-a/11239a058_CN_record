import socket

# Get host name
host_name = socket.gethostname()

# Get IP address
ip_address = socket.gethostbyname(host_name)

print("Host Name:", host_name)
print("IP Address:", ip_address)