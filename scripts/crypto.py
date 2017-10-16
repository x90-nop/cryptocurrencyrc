#!/usr/bin/python
#This script is part of cryptocurrencyrc for Conky: https://github.com/x90-nop/cryptocurrencyrc
import argparse
import BeautifulSoup
import requests
import sys
import os.path
import ConfigParser

prices_file_path = 'scripts/last_prices.txt'
prices_file = open(prices_file_path,'r+')
html_parse = '0123456789,.'
BTC_URL = 'https://coinmarketcap.com/currencies/bitcoin/'
ETH_URL = 'https://coinmarketcap.com/currencies/ethereum/'
XMR_URL = 'https://coinmarketcap.com/currencies/monero/'

Config = ConfigParser.SafeConfigParser()
Config.read(prices_file_path)

#Read and parse html content to extract currency price
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

#Calls get_price for the coin given in the -c arg
#coin_switch(coin, False) will return price
#coin_switch(coin, True) will return appreciation
def coin_switch(coin, _appreciation):
	open(prices_file_path, 'w').close() #clear previous file
	if Config.has_section('cryptorc')==False:
		Config.add_section('cryptorc')
	if(_appreciation == False):
		if(coin=='BTC'):
			Config.set('cryptorc','bitcoin',get_price(BTC_URL))
			Config.write(prices_file)
			return get_price(BTC_URL)
		elif(coin=='ETH'):
			Config.read(prices_file)
			Config.set('cryptorc','ethereum',get_price(ETH_URL))
			Config.write(prices_file)
			return get_price(ETH_URL)
		elif(coin=='XMR'):
			Config.set('cryptorc','monero',get_price(XMR_URL))
			Config.write(prices_file)
			return get_price(XMR_URL)
	else:
		if(coin=='BTC'):
			ap = 100.0-((float(Config.get('cryptorc','bitcoin'))/float(get_price(BTC_URL)))*100.0)
			return ap
		elif(coin=='ETH'):
			ap = 100.0-((float(Config.get('cryptorc','ethereum'))/float(get_price(ETH_URL)))*100.0)
			return ap
		elif(coin=='XMR'):
			ap = 100.0-((float(Config.get('cryptorc','monero'))/float(get_price(XMR_URL)))*100.0)
			return ap


#ArgParse settings
parser = argparse.ArgumentParser(description='Provides price info about cryptocurrencies')
parser.add_argument('-c', action = 'store', dest = 'currency', choices=['BTC', 'ETH', 'XMR'],
	required = True, help = 'Cryptocurrency abreviation(BTC,ETH or XMR).')
parser.add_argument('-a', action = 'store_true', dest='appreciation',
	required = False, help = 'If called,returns appreciation value instead of price')
args = parser.parse_args()

#"MAIN"
if(args.appreciation==True):
	if(os.path.isfile('/tmp/cryptorc')==False):
		open('/tmp/cryptorc', 'w')
		print "%.2f" % (coin_switch(args.currency, True))
	else:
		prices_file.close()
		quit()
else:
	print coin_switch(args.currency, False)
	prices_file.close()
