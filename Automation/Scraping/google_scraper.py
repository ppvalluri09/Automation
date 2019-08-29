import requests
from bs4 import BeautifulSoup
import os

URL = 'https://www.google.com/search?q='

headers = {
	"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}

query = str(input('Enter a search topic: '))
URL += query
query = query.split(' ')
query = '_'.join(query)
print(query)

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

link_div = soup.findAll("div", {"class": "r"})
links = []

for div in link_div:
	_links = div.findAll('a')
	for a in _links:
		if a['href'][:5] == 'https' or a['href'][:4] == 'http':
			if a['href'][:16] != 'https://webcache':
				links.append(a['href'])
print(links)

l = 0
if os.path.isdir(query) == False:
	os.mkdir(query)
else:
	dir_ = os.listdir(query)
	l = len(dir_)
	print('Directory already exists')

for i in range(len(links)):
	page_ = requests.get(links[i], headers = headers)
	soup_ = BeautifulSoup(page_.content, 'html.parser')
	title = query + str(i + l)
	print(title)
	path = query + "/" + title + ".html"
	with open(path, "w") as file:
		file.write(str(soup_))
