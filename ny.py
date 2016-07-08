import random
import requests, bs4
import re
import easygui
from Tkinter import *
from time import sleep


def script_scrape():
	#res = requests.get('http://www.laughfactory.com/jokes/')
	#res.raise_for_status()
	#news = bs4.BeautifulSoup(''.join(res), "lxml")
	#print news
	#news_set = news.findAll('a')
	#print_article('http://www.laughfactory.com/jokes/')
	#for x in news_set:
	#	print x
	#y = link_return(news_set)
	print_article('http://www.laughfactory.com/jokes/family-jokes/')
	#print_article(y)
	 

def link_return(news_set):
	st = random.choice(news_set)
	print st.get('href')
	return  st.get('href')

def print_article(y):
	
	res = requests.get(y)
	res.raise_for_status()
	jokes_soup = bs4.BeautifulSoup(''.join(res), "lxml")
	#print jokes_soup
	#type(jokes_soup)
	#elem = jokes_soup.select("div #joke3-pop-box")
	#print jokes_soup.div.div.p
	#print elem

	#print jokes_soup.findAll('p', attrs=re.compile('joke_'))

	t =  jokes_soup.findAll('p',id=lambda x:x and x.startswith('joke_'))
	#print t
	for x in t:

		print x.get_text()
		print '-------------------------------'

	
	link = jokes_soup.findAll('a')
	for x in link:
		print x.get('href')
	st  = link_return(link)
	req = requests.get(st)
	req.raise_for_status()
	jokes_html = bs4.BeautifulSoup(''.join(req), "lxml")
	y = jokes_html.findAll('a')
	link  = link + y
	#for x in y:
	#print_article(y[1])
	#print y[1]
			

	"""#print y
				res = requests.get(y)
				#print req.get_text()
				res.raise_for_status()
				article = bs4.BeautifulSoup(''.join(res), "lxml")
				art = article.findAll('p',id=lambda x:x and x.startswith('jokes_'))
				#print art.get_text()
				for x in art:
					print x.get_text()"""
		






script_scrape()	
	
