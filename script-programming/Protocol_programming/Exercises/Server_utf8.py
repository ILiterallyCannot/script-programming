import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 8888))
    sock.listen(5)
    (client, addr) = sock.accept()

    while True:
        data = client.recv(1024)
        if data == "":
            break
        print data.decode("utf-8", "replace")

main()
