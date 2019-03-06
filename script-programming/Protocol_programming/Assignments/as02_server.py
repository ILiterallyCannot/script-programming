import socket

def recvData (socks):
    client, addr = socks.accept()
    key = " "
    numberstr = ""

    while ord(key) != 3:
        key = client.recv(1)
        if ord(key) != 3:
            numberstr = numberstr + key
    datalen = int(numberstr)
    print("Data detected from {addr}, data length: {dl}".format(addr = addr[0], dl = numberstr))
    print datalen

    recvdData = ""
    while len(recvdData) < datalen:
        data = client.recv(1024)
        recvdData += data

    print(recvdData)
    print("Received {dbytes} bytes of data".format(dbytes = len(recvdData)))
    client.send("The server received this message {dbytes}".format(dbytes = len(recvdData)))
    client.close()

def main ():
    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    socks.bind(('localhost', 8888))
    socks.listen(5)
    print("Server is listening ...")
    ###while True:
    recvData(socks)
        ###print("Server is listening ...")
    socks.close()

if __name__ == "__main__":
    main()
