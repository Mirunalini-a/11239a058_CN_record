import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))
server_socket.listen(1)

print("Server ready for chat...")
conn, addr = server_socket.accept()
print("Connected to", addr)

while True:
    client_msg = conn.recv(1024).decode()
    if client_msg.lower() == "exit":
        break
    print("Client:", client_msg)

    reply = input("You: ")
    conn.send(reply.encode())

conn.close()