def send_data(socket, data):
        total = 0
        while total < len(data):
            sent = socket.send(data[total:])
            total += sent
        print "Sent %d bytes" % total

def send_message(socket, data):
        data_len = len(data)
        send_data(socket, str(data_len)+"\n")
        send_data(socket, data)

def read_length(socket):
        buffer =""
        while True:
                aid = socket.recv(1)
                if aid =="\n":
                        break
                buffer += aid
        return int(buffer)

def read_message(socket):
        buffer = ""
        length = read_length(socket)
        print "tavuja tulossa", length

        recieved = 0
        while recieved < length:
                data = socket.recv(1024)
                buffer += data
                recieved += len(data)

        return buffer
