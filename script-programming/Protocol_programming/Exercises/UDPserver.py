import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("localhost", 8888))

data, addr = s.recvfrom(1024)

print "%s, osoitteesta %s" % (data, addr)

s.sendto("terve T:server", addr)
