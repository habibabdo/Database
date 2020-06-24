import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='', database='salon')

mycursor = mydb.cursor()


mycursor.execute('select origin,destination,name  from flights LEFT JOIN passengers ON passengers.flight_id=flights.id ')

myresult = mycursor.fetchall()

print('Origin     Destination   name')

if myresult:
    print("LEFT JOIN Have Records:")
    for x in myresult:
        print(x)
else:
    print('No Records In Data Base')

mydb.close()
