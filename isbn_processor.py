#!/usr/bin/env python
import isbnlib
from isbntools.app import *

"""
File Name: isbn_processor.py
Purpose: To take in isbn's from a raw.txt file
        and output data into a isbn.txt file in
        a format that has informationa about the
        book
Modules Used:   isbnlib
                isbntools.app
"""


def clean_isbn(isbn_given):
    """
    This method is meant to clean the isbn up so it is
    usable in the MYSQL query

    :param isbn_given:
    :return:
    """
    query = isbn_given.replace(' ', '+')
    isbn_clean = isbn_from_words(query)
    return isbn_clean


def get_data(line):
    """
    Method to take the data from the MYSQL server and
    convert it from
    Type:       BOOK
    Title:      Why Should I Recycle
    Author:     Jen Green
    Author:     Mike Gordon
    ISBN:       9780764131554
    Year:       2005
    Publisher:  Barons Juveniles

    Into a dictionary to make data easily transferable
    {
        'Author': ['Jen Green', 'Mike Gordon'],
        'Type': 'BOOK',
        'Title': 'Why Should I Recycle?',
        'ISBN': '9780764131554',
        'Year': '2005',
        'Publisher': 'Barrons Juveniles'
    }

    :param line:
    :return:
    """
    # Book data dictionary
    book_data = {}

    # Using the isbntools.app, perform the query
    data_collected = registry.bibformatters['labels'](meta(line))

    # This is meant to be an echo to make sure the request
    # is what we were looking for
    # print(data_collected)

    # Split the data at the new lines
    iterated_data = data_collected.split("\n")
    # Type:BOOK

    # This is for authors, since there can be multiple
    book_data["Author"] = []

    # Loops through the data collected for the book
    # and converts it into a dictionary
    for data in iterated_data:
        if data.split(":")[0].strip() == "Author":
            book_data["Author"].append(data.split(":")[1].strip())
        else:
            book_data[data.split(":")[0].strip()] = data.split(":")[1].strip()
    return book_data


def write_book_to_file(dictonary):
    """
    Takes the dictionary created with get_data
    and saves it into a file to be accessed at
    a later time
    :param dictonary:
    :return:
    """
    with open("isbn.txt", "a") as isbn_txt:
        for value in dictonary.items():
            isbn_txt.write("{}:{}".format(value[0], value[1]))
            isbn_txt.write("\n")


def process_isbns():
    num_of_requests = 0
    try:
        last_isbn_tried = None
        with open("raw.txt") as raw_txt:
            for raw_line in raw_txt.readlines():
                num_of_requests += 1
                last_isbn_tried = clean_isbn(raw_line)
                try:
                    book_dict_results = get_data(last_isbn_tried)
                    write_book_to_file(book_dict_results)
                except isbnlib.dev._exceptions.NoDataForSelectorError:
                    print("{} does not exist".format(raw_line))
    except isbnlib.dev._exceptions.ISBNLibHTTPError:
        print("O no, you made {} request!".format(num_of_requests))
        print("We stopped at {} isbn.".format(last_isbn_tried))

# Need to add tester data
# Main file to run is process_isbns()
# The rest (clean_isbn, get_data, and writebook_to_file are helper methods
# fill raw.txt with the isbns that need to be processed, and isbn.txt
# will be filled with the data about the books, or nothing about them
