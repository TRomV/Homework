import socket
import random
import time
from random import choice
from string import ascii_letters


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind(('127.0.0.1', 50000))
serv_sock.listen(10)

client_sock, client_addr = serv_sock.accept()
i = 0

client_sock.sendall("Task 2. String length. Time to find the value of 2 seconds.\n".encode())

while i<20:
        i=i+1
        n = random.randint(10,150)
        stroka = ''.join(choice(ascii_letters) for i in range(n))

        s=len(stroka)
        print(s)

        print(stroka)
        
        client_sock.sendall(stroka.encode())
        client_sock.sendall("\n".encode())
        
        start = time.time()

        data = client_sock.recv(1024).decode()
                
        if time.time() - start >= 2:
                client_sock.sendall("You lose! Time!!!\n".encode())
                i=0
                time.sleep(0.5)
        
        else:
                if int(s) == int(data):
                        client_sock.sendall("Execcelent!\n".encode())
                        time.sleep(0.5)
                else:
                        client_sock.sendall("You lose!\n".encode())
                        i=0
                        time.sleep(0.5)

client_sock.sendall("FLAG".encode())
client_sock.close()
