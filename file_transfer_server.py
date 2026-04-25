import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12347))
server_socket.listen(1)

print("Server ready to receive file...")
conn, addr = server_socket.accept()
print("Connected to", addr)

with open("received_file.txt", "wb") as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

print("File received successfully")
conn.close()