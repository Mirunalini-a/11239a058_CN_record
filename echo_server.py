import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Echo Server is running...")

conn, addr = server_socket.accept()
print("Connected by", addr)

data = conn.recv(1024).decode()
print("Received:", data)

conn.send(data.encode())
conn.close()