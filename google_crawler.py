#!/usr/bin/env python

import urllib
import json

def get_google_results(i):
	base = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'
	query = urllib.urlencode({'q' : '-inurl:htm -inurl:html intitle:"index of" wsdl'})
	response = urllib.urlopen(base + query).read()
	data = json.loads(response)

	return data['responseData']['results'][i]['url']

def func_A():
	links = []
	for i in range(0, 3):
		links.append(get_google_results(i))

	return links