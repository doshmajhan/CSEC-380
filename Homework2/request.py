import socket

host = "54.209.150.110"
port = 80
CRLF = "\r\n\r\n"

def activity1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("POST / HTTP/1.1\nHost: %s%s" % (host, CRLF))
    data = s.recv(1000000)
    print data
    s.shutdown(1)
    s.close()

def activity2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("POST /getSecure HTTP/1.1\nHost: %s\nConnection: keep-alive%s"
            % (host, CRLF))
    data = s.recv(1000000)
    index = data.find('Your Security')
    token = data[index:-1].replace("Your Security Token is: ", "").strip()
    s.shutdown(1)
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    params = "token=%s" % token
    request = "POST /getFlag2 HTTP/1.1\r\n" \
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
    return data, token

def activity3(token):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    params = "token=%s" % token
    request = "POST /getFlag3Challenge HTTP/1.1\r\n" \
            "Content-Type: application/x-www-form-urlencoded\r\n" \
            "Content-Length: %s\r\n" \
            "Host: %s\r\n" \
            "Connection: close%s%s" \
            % (str(len(params)), host, CRLF, params)

    s.send(request)
    data = s.recv(1000000)
    s.shutdown(1)
    s.close()
    index = data.find("solve")
    data = data[index:-1]
    question = data.replace("solve the following: ", "")
    answer = eval(question)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    params += "&solution=%s" % str(answer)
    request = "POST /getFlag3Challenge HTTP/1.1\r\n" \
            "Content-Type: application/x-www-form-urlencoded\r\n" \
            "Content-Length: %s\r\n" \
            "Host: %s\r\n" \
            "Connection: close%s%s" \
            % (str(len(params)), host, CRLF, params)
    s.send(request)
    data = s.recv(1000000)
    print data

def activity4(token):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    params = "username=dos&token=%s" % token
    request = "POST /createAccount HTTP/1.1\r\n" \
            "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\n" \
            "Accept-Encoding: gzip, deflate\r\n" \
            "Accept-Language: en-US\r\n" \
            "Connection: Keep-Alive\r\n" \
            "Content-Type: application/x-www-form-urlencoded\r\n" \
            "Content-Length: %s\r\n" \
            "Host: %s\r\n" \
            "User-Agent: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)\r\n" \
            "Cache-Control: no-cache" \
            "%s%s" \
            % (str(len(params)), host, CRLF, params)

    s.send(request)
    data = s.recv(1000000)
    s.shutdown(1)
    s.close()
    index = data.find("password")
    data = data[index:]
    password = data.replace("password is ", "")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    password = password.replace("&", "%26")
    password = password.replace("=", "%3D")
    params = "token=%s&username=dos&password=%s" % (token, password)
    request = "POST /login HTTP/1.1\r\n" \
            "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\n" \
            "Accept-Encoding: gzip, deflate\r\n" \
            "Accept-Language: en-US\r\n" \
            "Connection: Keep-Alive\r\n" \
            "Content-Type: application/x-www-form-urlencoded\r\n" \
            "Content-Length: %s\r\n" \
            "Host: %s\r\n" \
            "User-Agent: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)\r\n" \
            "Cache-Control: no-cache" \
            "%s%s" \
            % (str(len(params)), host, CRLF, params)
    s.send(request)
    data = s.recv(1000000)
    s.shutdown(1)
    s.close()
    print data

if __name__ == '__main__':
    activity1()
    data, token = activity2()
    print data
    activity3(token)
    activity4(token)
