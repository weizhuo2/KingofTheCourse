#encoding=utf-8
# Written By WWZ - AUG 7 2017
import os
import urllib
import urllib2
import cookielib

def input_infos():
	username = raw_input("NetID: ")
	pw = raw_input("Password: ")
	return username,pw

username = ""
pw = ""

(username,pw) = input_infos()

postURL = "https://eas.admin.uillinois.edu/eas/servlet/login.do"
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
				'AppleWebKit/537.36 (KHTML, like Gecko) '
				'Chrome/59.0.3071.115 Safari/537.36',
	'Referer':'https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1'
}

form = {
	'inputEnterpriseId':username,
	'password':pw,
	'BTN_LOGIN':'Log+In'
}

#Creating a cookieJar
jar = cookielib.FileCookieJar('cookies')
handler = urllib2.HTTPCookieProcessor(jar)

#Prepare the form
coded_form = urllib.urlencode(form)

#Opening the website
opener = urllib2.build_opener(handler)
request = urllib2.Request(postURL, coded_form, headers)
website = opener.open(request)

#Some tools to debug
print '\nDebug tools\n'

#print website.read()

print website.headers
print jar

#save as HTML file
f = open('website.html','w')
f.write(website.read())
f.close()
print 'Page saved in app directory!'

#opening the file using web browser
print 'Opening the page...'
os.system('open website.html')





