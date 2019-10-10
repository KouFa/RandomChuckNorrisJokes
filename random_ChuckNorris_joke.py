import json
from urllib.request import urlopen

with urlopen('http://api.icndb.com/jokes/random') as response:
    data = json.loads(response.read())

print(data['value']['joke'])
