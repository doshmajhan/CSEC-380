import socket

host = "74.67.165.146"
#host = "54.84.187.188"
port = 1234
CRLF = "\r\n\r\n"
link = "http://54.226.56.246"

def send_link():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((host, port))
    params = "link=%s" % link
    request = "POST / HTTP/1.1\r\n" \
            "Content-Type: application/x-www-form-urlencoded\r\n" \
            "Content-Length: %s\r\n" \
            "Host: %s\r\n" \
            "User-Agent: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)\r\n" \
            "Connection: close%s%s" \
            % (str(len(params)), host, CRLF, params)

    s.send(request)
    data = s.recv(1000000)
    s.shutdown(1)
    s.close()
    return data

if __name__ == '__main__':
    data = send_link()
    print data
