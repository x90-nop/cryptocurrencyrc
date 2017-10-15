import BeautifulSoup
import requests
import re
import sys
filtro="0123456789,"
Soup = BeautifulSoup.BeautifulSoup
source = requests.get("http://dolarhoje.com/ethereum/")
soup = Soup(source.content)
BTC = str(soup.find(id='nacional'))
for c in BTC:
	if c in filtro:
		sys.stdout.write(c)
		sys.stdout.flush()
