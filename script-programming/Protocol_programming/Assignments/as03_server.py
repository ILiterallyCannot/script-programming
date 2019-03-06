import socket
import sys

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
    print("Received {dbytes}/{amount} bytes of data".format(dbytes = len(recvdData), amount=numberstr))
    if len(recvData) != datalen:
        print("Warning: Corrupted data!")

    client.close()

def main ():
    arg_count = len(sys.argv)
    if arg_count != 3:
        print("In order for this to work, it needs 2 arguments. For example in terminal: $ python client.py localhost 8888")
        return
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except Exception:
        print ("Error: Port is not valid.")
        print("In order for this to work, it needs 2 arguments. For example in terminal: $ python client.py localhost 8888")
        return
    try:
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        socks.bind(('localhost', 8888))
        socks.listen(5)
    except socket.error, errors:
        print ("Server failed to start. Error: " + errors.message)
        return
    print ("Server started!")
    print("Server is listening at {host} : {port}".format(host = host, port = port))
    ###while True:
    recvData(socks)
        ###print("Server is listening ...")
    socks.close()

if __name__ == "__main__":
    main()
