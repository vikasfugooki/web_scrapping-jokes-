import random
import requests, bs4
import re
import easygui
from Tkinter import *
from time import sleep
res = requests.get('http://www.laughfactory.com/jokes/family-jokes')
res.raise_for_status()
jokes_soup = bs4.BeautifulSoup(''.join(res), "lxml")
#type(jokes_soup)
#elem = jokes_soup.select("div #joke3-pop-box")
#print jokes_soup.div.div.p
#print elem

#print jokes_soup.findAll('p', attrs=re.compile('joke_'))

t =  jokes_soup.findAll('p',id=lambda x:x and x.startswith('joke_'))
'''for x in t:

	print x.get_text()
	print '-------------------------------'
	#with Tk (timeout=5)
	#easygui.textbox(msg=x.get_text(),title='jokes',codebox=0)
	#easygui.msgbox()
	#with Tk(timeout=5):
	easygui.msgbox(x.get_text())
	sleep(10)

'''



def retrieve_link ():
	t = jokes_soup.findAll('a')
	#for x in t:
		#print x.get_text()
		#print '------------------------------------'
	go_link(t)	




# function to go to other website
def go_link (t):
	x = random .choice(t)
	print x
	print '-------------------------'

retrieve_link()