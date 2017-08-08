#encoding=utf-8
# Written By WWZ - AUG 7 2017
import urllib2
import cookielib

def input_infos():
	username = raw_input("NetID: ")
	pw = raw_input("Password: ")
	return username,pw

username = ""
pw = ""
postURL = "https://eas.admin.uillinois.edu/eas/servlet/login.do"

(username,pw) = input_infos()

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

