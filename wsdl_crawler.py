import xml.etree.ElementTree as ET
import mysql.connector
import json
import sys
import google_crawler as A, populate_data as B
import requests
import urllib2
from bs4 import BeautifulSoup

def get_link(url):
   page = urllib2.urlopen(url)
   html_doc = page.read()
   soup = BeautifulSoup(html_doc)
   urllinks = []
   for link in soup.find_all('a'):
      link = link.get('href')
      link = str(link)
      urllinks.append(link)
   newlinks = []
   for i in urllinks:
      if "http://" not in i:
         i = url + i
      newlinks.append(i)
   return newlinks

def crawl_inside(link):
	urllinks = get_link(link)
	for link in urllinks:
		if ".wsdl" in str(link):
			B.func_B(link)

def func_C():
	links = A.func_A()

	crawl_inside('http://data.serviceplatform.org/wsdl_grabbing/seekda-wsdls/valid_WSDLs/')
	for link in links:
		crawl_inside(link)