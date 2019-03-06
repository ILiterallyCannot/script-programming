# -*- coding: utf-8 -*-
import socket
def send_data(sock,data):
    total=0
    while total < len(data):
        sent = sock.send(data[total:])
        total +=sent
    print "Sent %d bytes" % total

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost",8888))

message = u" 简化字 " * 1000
data = message.encode("utf-8")
send_data(sock, data)
sock.close()
