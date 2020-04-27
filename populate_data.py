import xml.etree.ElementTree as ET
import mysql.connector
import os
import json
import sys
import google_crawler as A, wsdl_crawler as C, extract_info as D, ontology as E

def populate_database(url_value, desc, team, cursor, conn):
	try:
		values = (url_value, desc, team)
		query = "INSERT IGNORE INTO URL_data(url_value, url_desc, url_team)"
		query += " VALUES(%s, %s, %s)"
		cursor.execute(query, values)
		print values
		conn.commit()
		# print 'hi'

	except mysql.connector.Error as err:
		print query
		print(err)
	except Exception as e:
		print(e)
		print sys.exc_traceback.tb_lineno 


def func_B(url):
	try:
		os.environ['http_proxy']=''

		mysql_config = {
			'user': 'root',
			'password': 'password',
			'host': '127.0.0.1',
			'database': 'WebService',
		}

		conn = mysql.connector.connect(**mysql_config)
		cursor = conn.cursor()

		url = str(url)
		desc_url = D.parse_url(url)

		populate_database(url, desc_url, 'z', cursor, conn)
		# E.func_E(url)

		conn.close()
		return
		
	except mysql.connector.Error as err:
		print query
		print(err)
	except Exception as e:
		print (e)

def func_B_for_script(url, desc):
	try:
		os.environ['http_proxy']=''

		mysql_config = {
			'user': 'root',
			'password': 'password',
			'host': '127.0.0.1',
			'database': 'WebService',
		}

		conn = mysql.connector.connect(**mysql_config)
		cursor = conn.cursor()

		url = str(url)
		desc_url = desc

		populate_database(url, desc_url, 'z', cursor, conn)
		# E.func_E(url)

		conn.close()
		return
		
	except mysql.connector.Error as err:
		print query
		print(err)
	except Exception as e:
		print (e)