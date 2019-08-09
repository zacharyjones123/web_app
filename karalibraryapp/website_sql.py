#!/usr/bin/env python
import sys
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')

import mysql.connector
from isbn_processor import get_book_list_from_file
from isbn_processor import get_data
from barcode_reader import scan_barcode_pi

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


def insert_new_books():
    """
    Used to add all books from isbn.txt into the database

    :return:
    """
    # using isbn_processor method to get dictionary
    # to access books easily
    book_list = get_book_list_from_file()
    for book in book_list:
        query = "INSERT INTO books (`Title`, `Author`, `ISBN`, `Year`, `Publisher`) VALUES (%s, %s, %s, %s, %s)"
        print(book)
        val = (book["Title"],book["Author"],book["ISBN"],book["Year"],book["Publisher"])
        mycursor.execute(query, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


def insert_into_database():
    """
    This method is to show the insert feature of
    the MySql database
    :return:
    """
    book_data = get_data(scan_barcode_pi())
                         
    
    query = "INSERT INTO books (`Title`, `Author`, `ISBN`, `Year`, `Publisher`) VALUES (%s, %s, %s, %s, %s)"
    val = (book_data["Title"], book_data["Author"][0], book_data["ISBN"], book_data["Year"], book_data["Publisher"])
    mycursor.execute(query, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
insert_into_database()


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



def __str__(self):
    return "Hello"


def __repr__(self):
    return "Hello"


def __format__(self, f):
    return "Hello"
