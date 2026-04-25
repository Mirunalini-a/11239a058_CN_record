import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12347))

with open("send_file.txt", "rb") as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)

print("File sent successfully")
client_socket.close()