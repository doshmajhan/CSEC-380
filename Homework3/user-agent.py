import csv
import requests
import threading
from bs4 import BeautifulSoup


all_links = set()
all_emails = set() 


def get_image(num, items):
    length = (num*7)+7
    if num == 9:
        length = len(items)
        
    lst = items[num*7:length]
    for img in lst:
        name = img.rsplit('/', 1)[-1]
        print 'Downloading: %s' % name
        r = requests.get('http://www.rit.edu/%s' % img, stream=True)
        with open('pics/%s'%name, 'wb') as f:
            for chunk in r:
                f.write(chunk)


def activity1():
    url = "https://www.rit.edu/programs/computing-security-bs"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
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
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
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


def activity2(domain, url, depth):
    global all_links
    global all_emails

    # we've reached max depth or were out of url scope
    if depth == 0:
        return None

    try:
        r = requests.get(url)

    # may have just gotten a relative path
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
        url = 'https://www.rit.edu/{}'.format(url)
        r = requests.get(url)
        return None

    except Exception as e:
        print e
        return None

    if domain not in url:
        print "NOT IN DOMAIN => {}".format(url)
        return None

    if url in all_links:
        return None

    all_links.add(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.findAll('a', href=True)
    emails = soup.select('a[href^=mailto]')
    for e in emails:
        if e['href'] not in all_emails:
            #print "EMAIL -> {}".format(e['href'])
            all_emails.add(e['href'])

    for l in links:
        print '{} -> {} ==> {}'.format(r.status_code, l['href'], depth)
        activity2(domain, l['href'], depth-1)
        

def activity3():
    f = open('companies.csv')
    reader = csv.reader(f)
    for row in reader:
        activity2(row[1], row[1], 4)
    
    print all_links

if __name__ == '__main__':
    #activity1()
    #activity2("rit.edu", "https://www.rit.edu/", 4)
    activity3()

