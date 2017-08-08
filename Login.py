#encoding=utf-8
# Written By WWZ - AUG 7 2017
import urllib
import urllib2
import cookielib

def input_infos():
	username = raw_input("NetID: ")
	pw = raw_input("Password: ")
	return username,pw

username = ""
pw = ""

postURL = "https://eas.admin.uillinois.edu/eas/servlet/login.do"
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
				'AppleWebKit/537.36 (KHTML, like Gecko) '
				'Chrome/59.0.3071.115 Safari/537.36',
	'Referer':'https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1'
}
form = {
	'inputEnterpriseId':'weizhuo2',
	'password':'sbsbsbsb',
	'BTN_LOGIN':'Log+In'
}

#(username,pw) = input_infos()

#Creating a cookieJar
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)

#Prepare the form
coded_form = urllib.urlencode(form)

#Opening the website
opener = urllib2.build_opener(handler)
request = urllib2.Request(postURL, coded_form, headers)
website = opener.open(request)

#print the website source code
#print website.read()

#save as HTML file
f = open('website.html','w')
f.write(website.read())
f.close()








