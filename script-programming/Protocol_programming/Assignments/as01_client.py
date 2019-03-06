import socket

data = raw_input("Write your message here: ")
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("localhost", 8888))

except Connectionerror:
	print("oops, something went wrong")

def send(s, data):
	total = 0
	while total < len(data):
	    sent = s.send(data[total:])
	    total += sent
	print "Sent %d bytes" % total

data_len=len(data)
send(s, str(data_len)+"\n")
send(s, data)
