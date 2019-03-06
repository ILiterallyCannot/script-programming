import socket
import time
import random
import sys

def sendData (socket, data):
    total = 0
    newdata = str(len(data)) + chr(3) + data
    while total < len(data):
        try:
            sent = socket.send(newdata[total:])
            total += sent
            print "Sent {total} / {datalen} bytes of data!".format(total = total, datalen = len(newdata))
        except socket.error, errornotice:
            print("Sending failed... Data sent {total}. Data length {data}. Error: {errors}".format(total = total, data = len(newdata), errors = errornotice))
            break

def createConn(sock, destination):
    tries = 0
    while True:
        try:
            sock.connect(destination)
            break
        except socket.error, errornotice:
            print("Failed! Try number {tries}, Msg: {errornotice}".format(tries = tries, errornotice = errornotice))
            tries+=1
            time.sleep(2)
    return sock

def strGenerator(amount):
    string = ''
    for x in range(0, amount):
        string = string + chr(65 + random.randrange(0, 20, 1))
    return string

def main ():
    arg_count= len(sys.argv)
    if arg_count != 4:
        print("In order for this to work, it needs 3 arguments. For example in terminal:$ python client.py localhost 8888 [size of data]")
        return
    host = sys.argv[1]
    try:
        port=int(sys.argv[2])
        stramount = int(sys.argv[3])
    except Exeption:
        print ("Error: Port or amount number not valid.")
        print("In order for this to work, it needs 3 arguments. For example in terminal:$ python client.py localhost 8888 [size of data]")
        return
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ## Wait for established connection.
        sock = createConn(sock, ('localhost', 8888))
        sendData(sock, strGenerator(5555))
    except Exception, socket.error:
        print("Error while sending! Msg: " + socket.error.message)

    sock.close()

if __name__ == "__main__":
    main()
