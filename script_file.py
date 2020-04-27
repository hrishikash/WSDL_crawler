import sys, os
import requests
from subprocess import *
import glob
import xml.etree.ElementTree as ET
import extract_info as D

def get_wsdl(cmd):
		p = Popen(cmd, shell=True, stdout=PIPE)
		output = p.communicate()[0]
		return output

def func_F():
	path = '/home/ashrithhcs/Desktop/wsdl_files/*.wsdl'
	files=glob.glob(path)
	for f in files:
		data = get_wsdl('cat '+f)
		D.parse_file(data)