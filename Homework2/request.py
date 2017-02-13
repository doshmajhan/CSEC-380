import socket

host = "54.209.150.110"
port = 80
CRLF = "\r\n\r\n"

def activity1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    #s.send("GET / HTTP/1.1%s Host: %s%s%s" % (CRLF, host, CRLF, CRLF))
    s.send("POST / HTTP/1.1\nHost: %s%s" % (host, CRLF))
    data = s.recv(1000000)
    print data
    s.shutdown(1)
    s.close()

def activity2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    #s.send("GET / HTTP/1.1%s Host: %s%s%s" % (CRLF, host, CRLF, CRLF))
    s.send("POST /getSecure HTTP/1.1\nHost: %s%s" % (host, CRLF))
    data = s.recv(1000000)
    print data
    s.shutdown(1)
    s.close()

if __name__ == '__main__':
    #activity1()
    activity2()
