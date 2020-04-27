#!/usr/bin/env python

import urllib
import json

base = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'
query = urllib.urlencode({'q' : '-inurl:htm -inurl:html intitle:"index of" wsdl'})
response = urllib.urlopen(base + query).read()
data = json.loads(response)

# print data
print data['responseData']['results'][1]['url']
# for i in range(0, 5):
#     print data['responseData']['results'][i]['url']
