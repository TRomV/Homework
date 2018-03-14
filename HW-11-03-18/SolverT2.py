import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 50000))

data = client_sock.recv(1024).decode()
print (data)
i=0
while i<20:
    i=i+1
    data = client_sock.recv(1024).decode()
    answer = str(len(data))
    client_sock.send(answer.encode())
    print (data)
    data = client_sock.recv(1024).decode()
    print (data)
    
data = client_sock.recv(1024).decode()
print(data)
input()
