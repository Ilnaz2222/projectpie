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




d = '♠'
e = '♣'
f = '♦' 
g = '♥'
trom=2
# type text

gn= 1

while True:
	b = ''
	if gn<149:
		gn += 1
	else:
		gn = 0
	a = ''
	kok = ''
	print (a)	

	bub=('♦')
	cherv=('♥')
	pik=('♠')
	tref=('♣')
	
	
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
