# UrlLib -> a library for http requests

import urllib, urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('https://google.com')
# for line in fhand:
#     print(line.decode().strip())

# BeautifulSoup -> a library for pulling data out of html and xml
# Used in conjunction with urllib to get data and then parse it

from bs4 import BeautifulSoup

url = 'https://google.com'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Get all b tags
tags = soup('b')
for tag in tags:
    print(tag)  # <b class="gb1">Search</b>

# This can be used to look for a tags and then get href elements to make a web spider!
# Finding URL's
print('Urls on page: ')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
