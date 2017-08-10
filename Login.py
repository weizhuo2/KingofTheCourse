# -*- coding: utf-8 -*-

import requests
import getpass
import re

loginURL = "https://eas.admin.uillinois.edu/eas/servlet/login.do"
#URL = "https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu&amp;msg=WELCOME+<b>Welcome,+Weizhuo+Wang,+to+UI-Integrate+Self-Service!<%2Fb>Aug+09,+201709%3A46+pm"

def get_payload():
	NID = raw_input("NetID: ")
	pw = getpass.getpass("Password: ")
	payload = {
		'inputEnterpriseId': NID, #NID
		'password': pw,			#pw
		'BTN_LOGIN':'Log+In'
	}
	return payload

def get_headers():
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
				'AppleWebKit/537.36 (KHTML, like Gecko) '
				'Chrome/59.0.3071.115 Safari/537.36',
		'Referer':'https://eas.admin.uillinois.edu/eas/servlet/login.do'
	}
	return headers

def LoadCookies():
	import cookielib
	jar = cookielib.MozillaCookieJar()
	jar.load('cookies.txt', ignore_discard=True, ignore_expires=True)
	return jar

def LoginSucceed(content):
	try:
		str1 = re.search('meta http-equiv="refresh" content="0;url=', content, flags=0).span()
	except AttributeError:
		return False
	else:
		str2_1 = re.search('bmenu', content, flags=0).span()
		str2_2 = re.search('&amp', content, flags=0).span()
		str3_1 = re.search('WELCOME', content, flags=0).span()
		str3_2 = re.search('">', content, flags=0).span()
		print 'Login Succeed.\n'
		nam = content[str2_1[0]:str2_2[0]]
		msg = content[str3_1[1]:str3_2[0]]
		pl = {'name':nam,'msg':msg}
		return (True,pl)

def SavePage(content,filename):
	f = open(filename,'w')
	f.write(content.encode('utf-8'))
	f.close()
	print 'Page saved in app directory!'

def OpenPage(filename):
	import os
	os.system('open '+filename)

def main():
	#Initialize
	headers = get_headers()
	session = requests.Session()
	#Load cookies using cookielib
	jar = LoadCookies()
	session.cookies = jar

	#post form
	payload = get_payload()
	loginPage = session.post(loginURL,payload,headers)
	#Is the login succeed?
	content = loginPage.text
	Success = LoginSucceed(content)


	if type(Success) == bool:
		print 'Login Failed, check your password and username.'
		#Unfinished here, return to login entering page
	elif type(Success) == tuple:
		pl = Success[1]
		menuPage = session.get('https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu',params = pl)
		print 'Jumping to: ', menuPage.url
		content = menuPage.text #Note that content temporarily holds source code of HTML page.
		SavePage(content,'menuPage.html')
		OpenPage('menuPage.html')



if __name__ == "__main__":
	main()
