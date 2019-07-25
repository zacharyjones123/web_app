import mysql.connector

"""
File Name: website_sql.py
Purpose:  To connect to my personal websites
          MySql database and testing basic
          functionality
"""

# database info
# Uses the mysql.connector.connect method
mydb = mysql.connector.connect(
  host="www.zacharyjones123.com",
  user="zrjones1_pycharm",
  passwd="wxH,+D0itryH",
  database="zrjones1_communicator"
)

# Cursor in order to traverse MySql database
mycursor = mydb.cursor(buffered=True)


def insert_into_database():
    """
    This method is to show the insert feature of
    the MySql database
    :return:
    """
    query = "INSERT INTO books (`Title`, `Author`, `ISBN`, `Year`, `Publisher`) VALUES (%s, %s, %s, %s, %s)"
    val = ('a', 'b', 'c', 'd', 'e')
    mycursor.execute(query, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def select_from_database():
    """
    This method is to demonstrate the SELECT method
    from MySql database
    :return:
    """
    query = "SELECT * FROM books;"
    mycursor.execute(query)
    result_set = mycursor.fetchall()

    for result in result_set:
        print(result)
    print(result_set)

