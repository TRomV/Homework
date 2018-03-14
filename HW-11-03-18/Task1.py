import socket
import random
import time

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind(('127.0.0.1', 50000))
serv_sock.listen(10)

client_sock, client_addr = serv_sock.accept()

client_sock.sendall("Task 1. Find 20 value of the expression to get the FLAG.\nTime to find the value of 2 seconds.".encode())

i = 0

while i<20:
        i=i+1
        a = random.randint(100,10000)
        b = random.randint(100,10000)
        summa = a+b
        print(a,b,summa)
        send_CL=str(a)+"+"+str(b)+"="
        client_sock.sendall(send_CL.encode())
        
        start = time.time()
        data = client_sock.recv(1024).decode()
        
        if time.time() - start >= 2:
                client_sock.sendall("You lose!\n".encode())
                i=0
                time.sleep(0.5)
        else:
                print (data)
                
                if int(summa) == int(data):
                        client_sock.sendall("Execcelent!\n".encode())
                        time.sleep(0.5)
                else:
                        client_sock.sendall("You lose!\n".encode())
                        i=0
                        time.sleep(0.5)

client_sock.sendall("FLAG".encode())
client_sock.close()
