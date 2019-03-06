VALID_METHODS=["GET","POST","PUT"]

request = "GET / HTTP/1.1"
status = "HTTP/1.1 200 OK"

def parse_request(line):
    parts = line.split(" ")
    if len(parts)!=3:
        print "Malformed request line"

    method = parts[0]
    resource = parts[1]
    version = parts[2]

    if method not in VALID_METHODS:
        print "Unknown HTTP Method"

    return (method, resource, version)

def validate_http_versions(version):
    if "/" not in version:
        print "Malformed HTTP version"
    (name,number) = version.split("/")

    if name != "HTTP":
        print "Malformed HTTP version"

    if "." not in number:
        print "Malformed HTTP version"

    return "Everything checks out"

print parse_request(request)
example = "HTTP/1.1"
print validate_http_versions(example)
