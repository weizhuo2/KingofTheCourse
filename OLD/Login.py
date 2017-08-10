#encoding=utf-8
# Written By WWZ - AUG 7 2017
import os
import re
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
	'Referer':'https://eas.admin.uillinois.edu/eas/servlet/login.do'
}

form = {
	'inputEnterpriseId':username,
	'password':pw,
	'BTN_LOGIN':'Log+In'
}

#Loading a cookieJar
jar = cookielib.MozillaCookieJar()
jar.load('cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib2.HTTPCookieProcessor(jar)

#Prepare the form
coded_form = urllib.urlencode(form)

#Opening the website
opener = urllib2.build_opener(handler)
request = urllib2.Request(postURL, coded_form, headers)
website = opener.open(request)

#print the content
content = website.read()
print content

try:
	success1 = re.search('meta http-equiv="refresh" content="0;url=', content, flags=0).span()
except AttributeError:
	print 'Login Failed, check your password and username.'
else:
	success2 = re.search('">', content, flags=0).span()
	print 'Login Succeed.\nMatched at:'
	print success1,success2
	add = content[success1[1]:success2[0]]
	HomePageURL = 'https://ui2web1.apps.uillinois.edu' + add
	print HomePageURL


'''
#Some tools to debug
print '\nDebug tools\n'

#print website.read()

print website.headers
print jar
'''
#save as HTML file

f = open('website.txt','w')
f.write(content)
f.close()
print 'Page saved in app directory!'
'''
#opening the file using web browser
print 'Opening the page...'
os.system('open website.html')
'''

