import requests

#r = requests.post('http://74.67.165.146:1234/board', data={'link':'<a href="http://54.226.46.246">hey</a>'})

r = requests.post('http://74.67.165.146:1234/', data={'message':'http://54.226.46.246'})

print r.status_code
print r.text

