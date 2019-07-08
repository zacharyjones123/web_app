#!/usr/bin/env python
import isbnlib
import sys
from isbntools.app import *


def get_data(line):
    book_data = {}
    query = line.replace(' ', '+')
    isbn = isbn_from_words(query)
    data_collected = registry.bibformatters['labels'](meta(line))
    print(data_collected)
    iterated_data = data_collected.split("\n")
    # Type:BOOK
    book_data["Book"] = iterated_data[1].split(":")[1].strip()
    # Author:Jen Green
    book_data["Author"] = iterated_data[1].split(":")[2].strip()
    # Author: Mike Gordon (can have multiple authors

    # ISBN:978....
    book_data["ISBN"] = iterated_data[1].split(":")[3].strip()

    # Year:2005
    book_data["Year"] = iterated_data[1].split(":")[4].strip()

    print(book_data)


get_data("9780764131554")


"""            
try:
    num_of_requests = 0
    last_isbn_tried = None
    with open("raw.txt") as raw_txt:
        for line in raw_txt.readlines():
            num_of_requests+=1
            last_isbn_tried = line
            try:
                query = line.replace(' ', '+')
                isbn = isbn_from_words(query)
                print(registry.bibformatters['labels'](meta(isbn)))
                with open("isbn.txt", "a") as isbn_txt:
                    isbn_txt.write("---{}---".format(line))
                    isbn_txt.write(registry.bibformatters['labels'](meta(isbn)))
                    isbn_txt.write("\n")
                    isbn_txt.write("-----------------")
            except isbnlib.dev._exceptions.NoDataForSelectorError:
                print("{l} does not exist".format(l=line))
except isbnlib.dev._exceptions.ISBNLibHTTPError:
    print("O no, you made {} request!".format(num_of_requests))
    print("We stopped at {} isbn.".format(last_isbn_tried))
"""