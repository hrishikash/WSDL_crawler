import sys
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import populate_data as B

def parse_url(url):
	data = requests.get(url)
	root = ET.fromstring(data.content)
	soup = BeautifulSoup(data.content, ['lxml', 'xml'])

	try:
		if soup.find_all('description') != []:
			return str(soup.find_all('description').text)
		elif soup.find_all('documentation') != []:
			return str(soup.find_all('documentation')[0].text)
		else:
			return "Description NOT FOUND IGNORE"
	except Exception as e:
		return "Description NOT FOUND IGNORE"

def parse_file(data):
	soup = BeautifulSoup(data)
	try:
		url = str(soup.find_all('soap:address')[0].get('location'))
		try:
			desc = str(soup.find_all('documentation')[0].text)
		except Exception as e1:
			desc = "Description NOT FOUNF IGNORE"
	except Exception as e2:
		return

	B.func_B_for_script(url, desc)