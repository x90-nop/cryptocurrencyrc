#!/usr/bin/python
#This script is part of cryptocurrencyrc for Conky: https://github.com/x90-nop/cryptocurrencyrc
import argparse
import BeautifulSoup
import requests

html_parse = '0123456789,.'
URL = 'https://coinmarketcap.com/currencies/'

def get_price(url, currency_name):
	html_source = requests.get(url+currency_name)
	Soup = BeautifulSoup.BeautifulSoup
	soup = Soup(html_source.content)
	cryptocurrency = str(soup.find(id='quote_price'))
	price = ''
	for c in cryptocurrency:
		if c in html_parse:
			price  += c
	return price;

parser = argparse.ArgumentParser(description='Provides price info about cryptocurrencies')
parser.add_argument('-c', action = 'store', dest = 'currency',
	required = True, help = 'Cryptocurrency full name(bitcoin,monero...)')
args = parser.parse_args()

print get_price(URL, args.currency)
