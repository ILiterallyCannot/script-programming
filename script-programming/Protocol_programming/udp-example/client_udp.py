import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto("Hello -Client",("localhost",8888))

data, addr = s.recvfrom(1024)

print data 
