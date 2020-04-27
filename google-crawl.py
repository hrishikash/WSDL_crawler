from google import search

links = []
for url in search('-inurl:htm -inurl:html intitle:"index of" wsdl', stop=20):
	print hi
	links.append(str(url))
for url in search('travel -inurl:htm -inurl:html intitle:"index of" wsdl', stop=20):
	links.append(str(url))
for url in search('hotel -inurl:htm -inurl:html intitle:"index of" wsdl', stop=20):
	links.append(str(url))
for url in search('restaurant -inurl:htm -inurl:html intitle:"index of" wsdl', stop=20):
	links.append(str(url))
for url in search('airlines -inurl:htm -inurl:html intitle:"index of" wsdl', stop=20):
	links.append(str(url))

# for url in links:
# 	print url

