import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

r = requests.get(url)

my_cookies = r.cookies
print(my_cookies)

r = requests.post(url,
    params={'p': 'login'},
    data={'username': 'dummy', 'password': '1234'},
    allow_redirects=False,
    cookies=my_cookies
    )
my_cookies = r.cookies
print(my_cookies)

r = requests.get(url,
    params={'p': 'protected'},
    cookies=my_cookies
)

print(r.text)