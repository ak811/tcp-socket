import socket
import os

serverName = socket.gethostname()
serverPort = 12356

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

file_name = input("Enter the file name: ")
clientSocket.send(file_name.encode())

client_file_path = input("Enter the path you wanna store the file: ")

response = clientSocket.recv(1024)
data = response.decode()
response_code = data.split('\n')[0]
print("From Server:", response_code)

html_content = data[len(data.split('\n')[0]):]

if response_code.encode().__eq__('200 ok'.encode()):
    full_path = client_file_path + '/' + file_name
    if not os.path.exists(client_file_path):
        os.makedirs(client_file_path)
        file = open(full_path, 'w', encoding='utf-8')
        file.write(html_content)
        file.close()
    pass

clientSocket.close()
