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

(username,pw) = input_infos()
