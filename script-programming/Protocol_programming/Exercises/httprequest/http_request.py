HTTP_VALID_METHODS =["GET","POST","PUT","DELETE","TRACE","OPTIONS","CONNECT"]

class HttpRequest:
    def __init__(self, method, resource="/", headers={}, body=None):
        self.method= method
        self.resource=resource
        self.headers=headers

        if method not in HTTP_VALID_METHODS:
            raise UnknownHTTPMethodException("invalid method")
        else:
            print "Request: Method was ok"

        if not "Host" in headers.keys(): #keys returns the list of all dict keys
            raise NoHostHeaderException()
        else:
            print "Request: Host header was ok"

    def write_to(self, f):
        print "Request: Requests write method"
        #https://tools.ietf.org/html/rfc7230#section-3.1.1
        f.write("%s %s HTTP/1.1\r\n" % (self.method,self.resource))
        write_header(f, self.headers)

        f.write("\r\n")
        f.flush() #empties the buffer and forces overwriting the file

        print "Request sent"

def write_header(f,headers):
    print "write_headers"
    for header, value in headers.iteritems():
        f.write("%s: %s\r\n" % (header, value))
class UnknownHTTPMethodException(Exception):
    pass
class NoHostHeaderException(Exception):
    pass
    #code blocks cannot be empty
