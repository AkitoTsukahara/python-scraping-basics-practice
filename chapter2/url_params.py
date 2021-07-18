import requests
from urllib.parse import quote, quote_plus

raw_string = 'a query with / , spaces and?&'
print(quote(raw_string))
print(quote_plus(raw_string))


url = 'http://www.webscrapingfordatascience.com/paramhttp/'
parameters = {
    'query': 'a query with / , spaces and?&'
}

r = requests.get(url, params = parameters)

print(r.url)
print(r.text)