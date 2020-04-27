# save this file as ......| test1.py
# run this file this way..| python  test1.py
import easygui as eg
import sys
import os
import mysql.connector

def get_urls(team):
    try:
        mysql_config = {
            'user': 'root',
            'password': 'password',
            'host': '127.0.0.1',
            'database': 'WebService',
        }

        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()

        query = "SELECT url_value FROM URL_data where url_team=\'"+str(team)+"\'"
        cursor.execute(query)
        data = cursor.fetchall()

        data_str = ''
        for i in data:
            print i
            data_str = data_str + str(i) + '\n'

        # os.system('')
        f = open('hello', 'r+')
        f.write(data_str)

        classify_service(data, conn, cursor)

        conn.close()
        return data
        
    except mysql.connector.Error as err:
        print query
        print(err)
    except Exception as e:
        print(e)    

while 1:
    title = "Message from test1.py"
    eg.msgbox("Welcome to WEB SERVICE SEARCH", title)

    msg ="Please select the category of web services which you would like to view"
    title = "Web Services Searching"
    choices = ["Travel", "Finance", "Communication", "Converter"]
    choice = eg.choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    #eg.msgbox("You chose: " + str(choice), "Survey Result")

    selected_option=str(choice)

    if(selected_option == 'Travel'):
        data = get_urls("Travel")
        # filename = os.path.normcase("c:/hello.txt")
        # f = open(filename, "r")
        # text = f.readlines()
        # f.close()
        eg.textbox(hello)
        # eg.textbox("Contents of file " + filename, "Show File Contents", text)
        

    if(selected_option == 'Finance'):
        get_urls("Finance")
        # filename = os.path.normcase("c:/finance.txt")
        # f = open(filename, "r")
        # text = f.readlines()
        # f.close()
        # eg.textbox("hello")
        # eg.textbox("Contents of file " + filename, "Show File Contents", text)        
        
    if(selected_option == 'Communication'):
        get_urls("Communication")
        # filename = os.path.normcase("c:/finance.txt")
        # f = open(filename, "r")
        # text = f.readlines()
        # f.close()
        # eg.textbox("hello")
        # eg.textbox("Contents of file " + filename, "Show File Contents", text)        
    

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel
