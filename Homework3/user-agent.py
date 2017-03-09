import csv
import requests
import socket
import ssl
import threading
from bs4 import BeautifulSoup


all_links = set()
all_emails = set() 

def get_data(host, request, https):
    ip = socket.gethostbyname(host)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    if https:
        sock = ssl.wrap_socket(sock)
        sock.connect((host, 443))
    else:
        sock.connect((host, 80))
    data = ""
    sock.send(request)
    while True:
        d = sock.recv(1024)
        if not d:
            break
        data += d
    
    sock.shutdown(1)
    sock.close()
    return data


def get_image(num, items):
    length = (num*7)+7
    if num == 9:
        length = len(items)

    lst = items[num*7:length]
    for img in lst:
        name = img.rsplit('/', 1)[-1]
        print 'Downloading: %s' % name
        img = img.replace(" ", "%20")
        request = "GET {} HTTP/1.1\r\n" \
                "Connection: keep-alive\r\n" \
                "User-Agent: python-requests/2.13.0\r\n" \
                "Host: www.rit.edu\r\n" \
                "Accept: image/jpeg,*/*\r\n\r\n".format("http://www.rit.edu"+img)

        data = get_data("rit.edu", request, False)
        data = data.rsplit('\r\n\r\n')
        with open('pics/%s' % name, 'wb') as f:
            f.write(data[1])


def activity1():
    url = "https://www.rit.edu/programs/computing-security-bs"
    request = "GET {} HTTP/1.1\r\n" \
            "Connection: close\r\n" \
            "User-Agent: python-requests/2.13.0\r\n" \
            "Host: www.rit.edu\r\n" \
            "Accept: */*\r\n\r\n".format(url)

    data = get_data("rit.edu", request, True)
    soup = BeautifulSoup(data, 'lxml')
    all_rows = soup.findAll('tr')
    for row in all_rows:
        tds = row.findAll('td')
        if len(tds) == 3:
            td1 = tds[0].get_text()
            td2 = tds[1].get_text()
            if td1 == u'\xa0':
                continue

            print td1, td2

    url = "https://www.rit.edu/gccis/computingsecurity/people"
    request = "GET {} HTTP/1.1\r\n" \
        "Connection: keep-alive\r\n" \
        "User-Agent: python-requests/2.13.0\r\n" \
        "Host: rit.edu\r\n" \
        "Accept: */*\r\n\r\n".format(url)

    data = get_data("rit.edu", request, True)
    
    soup = BeautifulSoup(data, 'lxml')
    divs = soup.findAll('div', {'class': 'staff-picture'})
    pics = []
    for d in divs:
        pic = d.findAll('img')
        pics += [pic[0]['src']]

    threads = []
    for i in range(10):
        t = threading.Thread(target=get_image, args=(i, pics))
        threads.append(t)
        t.start()


def activity2(domain, base, url, depth, f=None, https=False):
    # we've reached max depth or were out of url scope
    if depth == 0:
        return None

    if "http" not in url and "https" not in url:
        try:
            if base[-1] == '/':
                base = base[:-1]
            if url[0] != '/':
                base = base + '/'
        except:
            pass

        new_url = base + url
    else:
        new_url = url
    
    request = "GET {} HTTP/1.1\r\n" \
        "Connection: close\r\n" \
        "User-Agent: python-requests/2.13.0\r\n" \
        "Host: {}\r\n" \
        "Accept: */*\r\n\r\n".format(new_url, domain) 
    
    if domain not in new_url:
        #print "URL {} NOT IN DOMAIN {}".format(new_url, domain)
        return None
    
    try:
        data = get_data(domain, request, https)

    except Exception as e:
        print e
        return None

    data = data.split('\r\n\r\n', 1)
    all_links.add(url)
    if f:    
        f.write('{}\n'.format(url))
    
    try:
        status = data[0].split("\r\n")[0].split(" ")[1]
        print '{} -> {} ==> {}'.format(status, new_url, depth)
    except Exception as e:
        print "Error: {}".format(str(e))
    
    if len(data) != 2:
        return None

    soup = BeautifulSoup(data[1], 'lxml')
    links = soup.findAll('a', href=True)
    emails = soup.select('a[href^=mailto]')
    for e in emails:
        if e['href'] not in all_emails:
            print "EMAIL -> {}".format(e['href'])
            all_emails.add(e['href'])

    for l in links:
        if l['href'] in all_links:
            #print "Already have -> {}".format(url)
            continue

        activity2(domain, base, l['href'], depth-1, f=f, https=https)


def activity3():
    f = open('companies.csv')
    output = open('link_list.txt', 'a+')
    reader = csv.reader(f)
    for row in reader:
        domain = row[1]
        
        if "https" in domain:
            https = True
        else:
            https = False
        
        domain = domain.replace('http://', '')
        domain = domain.replace('https://', '')
        domain = domain.replace('www.', '')
        domain = domain.replace('/', '')
        domain = domain.strip()
       
        activity2(domain, row[1].strip(), row[1].strip(), 4, f=output, https=https)

    f.close()
    output.close()
    print all_links


def activity4():
    f = open('link_list.txt', 'r+')
    output = open('found_dirs.txt', 'a+')
    domain = '52.23.205.104'
    for line in f:
        line = line.replace("http://", "")
        line = line.replace("https://", "")
        paths = line.strip().split('/')
        for p in paths:
            if p == '':
                continue
            if p[0] == '?':
                continue

            url = "http://{}/{}".format(domain, p)
            request = "GET {} HTTP/1.1\r\n" \
                "Connection: close\r\n" \
                "User-Agent: python-requests/2.13.0\r\n" \
                "Host: {}\r\n" \
                "Accept: */*\r\n\r\n".format(url, domain) 
            
            data = get_data(domain, request, False)
            if "404" in data:
                print "404 => {}".format(url)
            else:
                print "200 FOUND URL => {}".format(url)
                output.write("{}\n".format(url))

    f.close()
    output.close()

if __name__ == '__main__':
    #activity1()
    #activity2("csec.rit.edu", "https://csec.rit.edu", "https://csec.rit.edu/", 1)
    #print(all_emails)
    #activity3()
    activity4()

