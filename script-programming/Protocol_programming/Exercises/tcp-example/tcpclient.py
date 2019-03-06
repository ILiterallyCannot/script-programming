import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("localhost", 8888))

s.send("Hello")

print s.recv(1024)

s.close()
