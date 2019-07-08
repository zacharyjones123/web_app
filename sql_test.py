import mysql.connector

mydb = mysql.connector.connect(
  host="www.zacharyjones123.com",
  user="zrjones1_wrdp1",
  passwd="OwzbtitvYnQuEo",
  database="zrjones1_communicator"
)

mycursor = mydb.cursor(buffered=True)

"""
sql = "INSERT INTO books (`Title`, `Author`, `ISBN`, `Year`, `Publisher`) VALUES (%s, %s, %s, %s, %s)"
val = ('a', 'b', 'c', 'd', 'e')
mycursor.execute(sql, val)
"""
query = "SELECT * FROM books;"
mycursor.execute(query)
resultSet = mycursor.fetchall()

for result in resultSet:
  print(result)


mydb.commit()

print(resultSet)

print(mycursor.rowcount, "record inserted.")