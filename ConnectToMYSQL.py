import mysql.connector

if mysql.connector.connect(host='localhost', user='root', passwd='', database='salon'):
    print('OK connected')
else:
    print('Cannot connect')

#print(mydb)

# mydb.close()
