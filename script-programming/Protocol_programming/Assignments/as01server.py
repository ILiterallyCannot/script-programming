import socket


def main():
        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("localhost", 8888))
            sock.listen(5)


            while True:
                (client, addr) = sock.accept()
                print "New connections from", addr



                message = client.recv(1)
                while not "\n" in message:
                        message += client.recv(1)

                bytes = 0
                bytes = int(message)
                print "%d bytes incoming" % bytes

                read = 0
                messagebuffer=""
                while read < bytes:
                        data = client.recv(1024)
                        messagebuffer += data
                        read += len(data)
                print "recieved %d bytes" % read

        except SocketError:
                print "Connection error"
        #client.send("got it. Server")
        client.close()
        sock.close()

main()
