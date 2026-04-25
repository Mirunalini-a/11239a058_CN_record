import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Server is running on port 8080...")

while True:
    client_socket, addr = server_socket.accept()
    request = client_socket.recv(1024).decode()
    print("Request received:\n", request)

    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
    response += "<h1>Hello from Server</h1>"

    client_socket.send(response.encode())
    client_socket.close()