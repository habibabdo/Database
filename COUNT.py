import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='', database='salon')

mycursor = mydb.cursor()

mycursor.execute('select flight_id  FROM  passengers GROUP BY flight_id HAVING COUNT(*) > 1')

myresult = mycursor.fetchall()

if myresult:

    print('COUNT  Have Records:')
    print('FLIGHT ID')
    print('_______________')
    for x in myresult:
        print(x[0])
    # print('</td></tr></table>')

else:
    print('No Records In Data Base')

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM  flights WHERE id IN ( SELECT  id FROM passengers GROUP BY flight_id HAVING  COUNT(*) > 1)')

myresult = mycursor.fetchall()

if myresult:

    print('COUNT  Have Records:')
    print('FLIGHT ID')
    print('_______________')
    for x in myresult:
        print(x)


else:
    print('No Records In Data Base')