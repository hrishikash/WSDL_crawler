import urllib2
from bs4 import BeautifulSoup

# fish_url = 'http://www.opennirvana.com'
# fish_url = 'http://www.jeevanksh.com/'
# fish_url = 'https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=beautifulsoup%20crawler'
# fish_url = 'http://www.thepythontree.in/source-code-9-web-crawler-with-python-using-beautifulsoup-module/'
# fish_url = 'http://schemas.opengis.net/wfs/1.1.0/wsdl/'
# fish_url = 'http://wisebed.eu/api/wsdl/iwsn/current/'
fish_url = 'http://data.serviceplatform.org/wsdl_grabbing/seekda-wsdls/valid_WSDLs/'
# fish_url = 'http://schemas.opengis.net/wfs/1.1.0/wsdl/example-GET-endpoints.wsdl'

def get_link(url):
   page = urllib2.urlopen(url)
   html_doc = page.read()
   soup = BeautifulSoup(html_doc)
   urllinks = []
   for link in soup.find_all('a'):
   # for link in soup.findAll({"class":"Rm"}):
      link = link.get('href')
      link = str(link)
      # if links.startswith('/') or fish_url in links:
         # urllinks.append(links)
      urllinks.append(link)
   newlinks = []
   for i in urllinks:
      if "http://" not in i:
         i = fish_url + i
      newlinks.append(i)
   return newlinks

links = get_link(fish_url)

# newlinks = []
# for i in links:
#    if "http://" not in i:
#       i = fish_url + i
#    newlinks.append(i)

   # newlinks = list(set(newlinks))
   # del links[:]

   # for j in newlinks:
   #    links = get_link(j)
   #    for k in links:
   #       if fish_url not in k:
   #          k = fish_url + k
   #       if k not in newlinks:
   #          newlinks.append(k)

# print newlinks
for l in links:
	print l