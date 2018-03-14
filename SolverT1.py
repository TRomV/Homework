import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 50000))

data = client_sock.recv(1024).decode()
print (data)

while True:
    data = client_sock.recv(1024).decode()
    data=data[0:-1]
    answer=str(eval(data))
    client_sock.send(answer.encode())
    print (data)
    data = client_sock.recv(1024).decode()
    print (data)
