import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='', database='salon')

mycursor = mydb.cursor()

mycursor.execute('select origin,destination,name  from flights JOIN passengers ON passengers.flight_id=flights.id')

myresult = mycursor.fetchall()

if myresult:

    print('JOIN  Have Records:')
    print('Origin   | Destination   |   namr')
    print('_______________________________')
    for x in myresult:
        print('     | ' + x[0]+'  | ' + x[1] + '  | ' + x[2])
    # print('</td></tr></table>')

else:
    print('No Records In Data Base')


mycursor.execute("select origin,destination,name  from flights JOIN passengers ON passengers.flight_id=flights.id  WHERE name = 'Alice'")

myresult = mycursor.fetchall()
print('Origin     Destination   name')
if myresult:
    print('Have Records:')
    for x in myresult:
        print('|' + x[0]+'|' + x[1] + '|' + x[2])
    # print('</td></tr></table>')

else:
    print('No Records In Data Base')

    mycursor.execute(
        "select origin,destination,name  from flights LEFT JOIN passengers ON passengers.flight_id=flights.id ")

    myresult2 = mycursor.fetchall()
    print('Origin     Destination   name')
    if myresult2:
        print("LEFT JOIN Have Records:")
        for x in myresult2:
            print('|' + x[0] + '|' + x[1] + '|' + x[2])
        # print('</td></tr></table>')

    else:
        print('No Records In Data Base')

mydb.close()
