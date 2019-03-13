# -*- coding: utf-8 -*-
import random
import telebot
from telebot import types
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
token = '755725557:AAEoh8sDS-JyNcXA3ss5KQxIyxlXmt1ON34'
owner = '-1001162659557'
bot = telebot.TeleBot(token)
base_url = "https://bkstat.vip/auth/vk"

login = "79625715221"
password = "inasfess2001"
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get(base_url)

d = '♠'
e = '♣'
f = '♦' 
g = '♥'
trom=2
# type text
text_area = driver.find_element_by_name('email')
text_area.send_keys(login)
 
text_area = driver.find_element_by_name('pass')
text_area.send_keys(password)
# click submit button
submit_button = driver.find_elements_by_id('install_allow')[0]
submit_button.click()
driver.get('https://bkstat.vip/21/stat')

a = ''
gn= 1

while True:
	b = ''
	if gn<149:
		gn += 1
	else:
		gn = 0
	a = ''
	kok = ''
	time.sleep(3)
	res = driver.execute_script("return document.documentElement.outerHTML")
	soup = BeautifulSoup(res, 'lxml')
	#box = soup.find('div', {'id': 'root'})
	for div in soup.find_all('div',attrs={'class': 'rt-td'}) :
		c = div.text
		result = re.findall(r'[♥♦♣♠]',c)
		ac = len(kok)
		if ac < 2:
			kok =result
		else:
			a = result
			break 
	print (a)	
	kl = a
	kl=(", ".join(kl)) 
	a = a[0:2]
	a=(", ".join(a)) 
	bub=('♦')
	cherv=('♥')
	pik=('♠')
	tref=('♣')
	#бубы
	bb=('♦, ♦')
	bt=('♦, ♣')
	bp=('♦, ♠')
	bc=('♦, ♥')
	#червы
	cb=('♥, ♦')
	ct=('♥, ♣')
	cp=('♥, ♠')
	cc=('♥, ♥')
	#Треф
	tt=('♣, ♣')
	tp=('♣, ♠')
	tb=('♣, ♦')
	tc=('♣, ♥')
	#Пик
	pp=('♠, ♠')
	pt=('♠, ♣')
	pb=('♠, ♦')
	pc=('♠, ♥')
	#if a ==tt:
	#	b =tref
	#elif a ==pp:
	#	b =cherv
	#elif a ==cc:
	#	b =pik
	#elif a ==bb:
	#	b=pik
	#elif a ==tp:
	#	b=cherv
	#elif a ==tc:
	#	b=tref
	#elif a ==tb:
	#	b=bub
	#elif a ==pt:
	#	b=tref
	#elif a ==pc:
	#	b=tref
	#elif a ==pb:
	#	b=bub
	#elif a ==ct:
	#	b=tref
	#elif a ==cp:
	#	b=cherv
	#elif a ==cb:
	#	b=pik
	#elif a ==bt:
	#	b=cherv
	#elif a ==bp:
	#	b=tref
	#elif a ==bc:
	#	b=cherv
	
	hj = random.randint(1,4)
	if hj == 1:
		b = tref
	elif hj == 2:
		b = pik
	elif hj == 3:
		b = cherv
	elif hj == 4:
		b = bub
	otvet = ("Номер игры👆.У Игрок -")
	
	b = (otvet+b)
	print(gn,'-----------')
	print(b)
	bot.send_message(owner, gn)
	bot.send_message(owner, b)
	time.sleep(117)
	





if __name__ == '__main__':
	bot.polling(none_stop = True)
