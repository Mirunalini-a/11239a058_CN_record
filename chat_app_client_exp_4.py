import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12346))

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())

    if msg.lower() == "exit":
        break

    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

client_socket.close()