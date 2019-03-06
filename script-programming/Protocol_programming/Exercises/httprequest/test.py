# -*- coding; utf-8 -*-
from http_request import HttpRequest
import socket

def main():
    host = "httpbin.org"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,80))
    req = HttpRequest("GET","/",headers={"Host": host, "Connection":"Close" })

    f = sock.makefile()
    req.write_to(f)

    for line in f:
        print line

    f.close()
    sock.close()

main()
