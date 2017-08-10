# -*- coding: utf-8 -*-
import re, urllib2, HTMLParser

def match_regex(pattern, url):
	html_parser = HTMLParser.HTMLParser()
	match_list = []
	src = urllib2.urlopen(url)
	html = src.read()
	charset_pat = re.compile(r'charset=(.*?)"', re.I|re.S)
	charset = charset_pat.findall(html)[0]
	charset.replace('"', '')
	if charset == 'gbk' or charset == 'GBK':
		charset = 'gb18030'
	html = html.decode(charset).encode('utf8')
	html = html_parser.unescape(html)
	com = re.compile(pattern, re.I|re.S)
	match_list = com.findall(html)
	src.close()
	return match_list