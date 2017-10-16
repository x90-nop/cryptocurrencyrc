#!/usr/bin/python
#This script is part of cryptocurrencyrc for Conky: https://github.com/x90-nop/cryptocurrencyrc
import argparse
import BeautifulSoup
import requests
import sys
import os.path

html_parse = '0123456789,.'
BTC_URL = 'https://coinmarketcap.com/currencies/bitcoin/'
ETH_URL = 'https://coinmarketcap.com/currencies/ethereum/'
XMR_URL = 'https://coinmarketcap.com/currencies/monero/'

def get_price(url):
	html_source = requests.get(url)
	Soup = BeautifulSoup.BeautifulSoup
	soup = Soup(html_source.content)
	cryptocurrency = str(soup.find(id='quote_price'))
	price = ''
	for c in cryptocurrency:
		if c in html_parse:
			price  += c
	return price;

def coin_switch(coin):
		if(coin=='BTC'):
			return get_price(BTC_URL)
		elif(coin=='ETH'):
			return get_price(ETH_URL)
		elif(coin=='XMR'):
			return get_price(XMR_URL)


parser = argparse.ArgumentParser(description='Provides price info about cryptocurrencies')
parser.add_argument('-c', action = 'store', dest = 'currency', choices=['BTC', 'ETH', 'XMR'],
	required = True, help = 'Cryptocurrency abreviation(BTC,ETH or XMR).')
args = parser.parse_args()

print coin_switch(args.currency)
