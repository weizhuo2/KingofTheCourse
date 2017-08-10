# -*- coding: utf-8 -*-

import requests
import getpass

loginURL = "https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1"
URL = "https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu"

def get_payload():
	NID = input("NetID: ")
	pw = getpass.getpass("Password: ")
	payload = {
		'inputEnterpriseId': NID,
		'password': pw,
		'BTN_LOGIN':'Log In'
	}
	return payload

def get_headers():
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Connection': 'keep-alive',
		'Host': 'ui2web1.apps.uillinois.edu',
		'Referer': 'https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1'
	}
	return headers

def main():
	headers = get_headers()
	payload = get_payload()
	session = requests.Session()
	loginPage = session.post(
		loginURL,
		data = payload,
		headers = headers
	)
	print(loginPage.status_code)
	menuPage = session.get(
		URL,
		headers = headers
	)
	print(menuPage.status_code)

if __name__ == "__main__":
	main()
