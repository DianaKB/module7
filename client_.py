import socket
import threading

def read_sok(sor):
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))
         
server = '127.0.0.1', 5431  
alias = input("Введите псевдоним: ") 
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sor.sendto((alias+' Connect to server').encode('utf-8'), server)
threading.Thread(target=read_sok,args=(sor,), daemon=True).start()
while True:
    mensahe = input("Сообщение: ")
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)


