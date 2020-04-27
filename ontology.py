import mysql.connector
import sys
import extract_info as D

def get_team(info):
	words = info.split()

	hash_ont = {0:'Travel', 1:'Finance', 2:'Communication', 3:'Converter'}

	ONTOLOGY  = [
				["travel", "hotel", "room", "reservation", "flight", "ticket", "fare", "agency", "currency", "exchange", "booking", "airport", "rental", "roombook", "restaurant", "meal", "parking", "car agency" , "weather"],
				["finance", "stock", "quote", "currency", "fiscal", "bank", "account", "principal", "instrument", "credit", "card", "economic"],
				["messenger", "contact", "instant", "email", "spam", "notification", "telecom"],
				["converter"]
				]

	team = ''
	for i in range(0, 3):
		for w in ONTOLOGY[i]:
			if w in words:
				team = team + hash_ont[i] + " "
				break

	return team

def classify_service(rows, conn, cursor):
	for row in rows:
		team = str(get_team(row[1]))
		print team
		try:
			# values = (team)
			# if team != '':
			query = "UPDATE URL_data SET url_team=\'"+(team)+"\' WHERE url_value=\'"+str(row[0])+"\'"
			cursor.execute(query)
			conn.commit()

		except mysql.connector.Error as err:
			print query
			print(err)
		except Exception as e:
			print(e)
			print sys.exc_traceback.tb_lineno 

		

def func_E():
	try:
		mysql_config = {
			'user': 'root',
			'password': 'password',
			'host': '127.0.0.1',
			'database': 'WebService',
		}

		conn = mysql.connector.connect(**mysql_config)
		cursor = conn.cursor()

		query = "SELECT * FROM URL_data where 1"
		cursor.execute(query)
		data = cursor.fetchall()

		classify_service(data, conn, cursor)

		conn.close()
		
	except mysql.connector.Error as err:
		print query
		print(err)
	except Exception as e:
		print(e)