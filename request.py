import requests
s = requests.Session()
r = s.get('https://twitter.com/elonmusk')
with open('test.html', 'w') as f: 
    f.write(r.text)