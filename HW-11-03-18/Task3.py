import socket
import random
import time
import pypyodbc

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind(('127.0.0.1', 50000))
serv_sock.listen(10)

client_sock, client_addr = serv_sock.accept()

client_sock.sendall("Task 3.Time to find the value of 2 seconds.\n".encode())

i = 0

while i<20:
        i=i+1
        
        connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=DESKTOP-K985Q12\SQLEXPRESS;'
                                      'Database=Hw;')
        a=random.randint(1,10)
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dbo.asdf WHERE id={};".format(a))
        row = cursor.fetchone()

        print(row)

        send_CL=str(row[1])+"\n"
        client_sock.sendall(send_CL.encode())
        
        start = time.time()
        data = client_sock.recv(1024).decode()

        if time.time() - start >= 3:
                client_sock.sendall("You lose!\n".encode())
                i=0
                time.sleep(0.5)
        else:
                r=str(row[2].split())
                d=str(data.split())
                print(r,d)        
                if r==d:
                        client_sock.sendall("Execcelent!\n".encode())
                        time.sleep(0.5)
                else:
                        client_sock.sendall("You lose!\n".encode())
                        i=0
                        time.sleep(0.5)

client_sock.sendall("FLAG".encode())
client_sock.close()
