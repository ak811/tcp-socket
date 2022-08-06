import socket
import os

serverPort = 12356

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(3)

print("Serverport", serverPort)

print("The Server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("new address :", addr[1])

    file_name = connectionSocket.recv(1024).decode()
    file_path = 'server_files/' + file_name

    if os.path.exists(file_path):
        message = '200 ok\n'
        connectionSocket.send(message.encode())

        file = open(file_path, "rb")
        data = file.read(1024)
        while data:
            connectionSocket.send(data)
            data = file.read(1024)

    else:
        message = '404 NOT FOUND'
        connectionSocket.send(message.encode())

    connectionSocket.close()
