#!/usr/bin/env python
# https://pypi.org/project/isbntools/
from isbntools.app import registry
from isbntools.app import meta
from isbnlib.dev import NoDataForSelectorError
from isbnlib.dev import ISBNLibHTTPError


# Global variable to use for barcode

"""
File Name: isbn_processor.py
Purpose: To take in isbn's from a raw.txt file
        and output data into a isbn.txt file in
        a format that has information about the
        book
Modules Used:   isbnlib
                isbntools.app
"""


def clean_isbn(isbn_given):
    """
    This method is meant to clean the isbn up so it is
    usable in the MYSQL query

    >>> clean_isbn("978-3-16-148410-0")
    '9783161484100'
    >>> clean_isbn("9783161484100")
    '9783161484100'
    >>> clean_isbn("978-3161484100")
    '9783161484100'
    >>> clean_isbn("9-7-8-3-1-6-1-4-8-4-1-0-0")
    '9780883855119'
    >>> clean_isbn("9-7-8-3-1-6-1484100")
    >>> clean_isbn("978-3-1-6-1484100")
    '9783161484100'

    :param isbn_given: isbn to be processed
    :return: returns an isbn that is only numbers
    """
    # query = isbn_given.replace(' ', '+')
    # isbn_clean = isbn_from_words(query)

    # Just using this as a way to look up books,
    # so where the - or spaces are will not matter
    # so this method will not try to keep this info

    # Need to go through all of the tests to see if a true
    # isbns

    # Test 1: 13 digits
    if len(isbn_given) != 13:
        return ""  # "Test 1 failed: ISBN not 13 digits"

    # Test 2: first 3 digits 978 or 979
    if isbn_given[0:3] != "978" and isbn_given[0:3] != "979":
        return ""  # "Test 2 failed: First three digits not 978 or 979

    def find_check_digit(isbn_test):
        check_digit = 0
        mult_by = 1
        for i in isbn_test[:-1]:
            num_i = int(i)
            check_digit += num_i * mult_by
            if mult_by == 1:
                mult_by = 3
            else:
                mult_by = 1
        return str(10 - check_digit % 10)

    # Test 3: Check Modulus 10
    if find_check_digit(isbn_given) != isbn_given[-1]:
        return ""  # "Test 3 failed: check digit

    return isbn_given


def add_book(line):
    write_book_to_file(get_data(line))


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
    print(book_data)
    return book_data


def write_book_to_file(dictionary):
    """
    Takes the dictionary created with get_data
    and saves it into a file to be accessed at
    a later time
    :param dictionary:
    :return:
    """
    with open("isbn.txt", "a") as isbn_txt:
        for value in dictionary.items():
            isbn_txt.write("{}:{}".format(value[0], value[1]))
            isbn_txt.write("\n")


def get_book_list_from_file():
    new_dict = []
    with open("isbn.txt", "r") as isbn_txt:
        counter = 0
        new_temp_dict = {"Title": "Nah",
                         "Author": "Nah",
                         "ISBN": "Nah",
                         "Type": "Nah",
                         "Year": 1000,
                         "Publisher": "Nah"
                         }
        for line in isbn_txt:
            line_split = line.split(":")
            print(line)
            new_temp_dict[line_split[0]] = line_split[1]
            counter += 1
            if counter == 6:
                new_dict.append(new_temp_dict)
                counter = 0
                new_temp_dict = {}
    return new_dict


def process_isbns():
    # Type Error = invalid ISBN number
    # isbnlib.dev._exceptions.ISBNNotConsistentError = not sure of this error yet
    num_of_requests = 0
    last_isbn_tried = "0000000000000"
    raw_txt = open("raw.txt")
    try:
        while True:
            raw_line = raw_txt.readline()
            num_of_requests += 1
            last_isbn_tried = clean_isbn(raw_line)
            try:
                book_dict_results = get_data(last_isbn_tried)
                write_book_to_file(book_dict_results)
            except NoDataForSelectorError:
                print("{} does not exist".format(raw_line))
                with open("not_found.txt", "w") as not_found_txt:
                    not_found_txt.write(last_isbn_tried)
                    not_found_txt.write("\n")
                # Need to finish reading the file

    except ISBNLibHTTPError:
        print("O no, you made {} request!".format(num_of_requests))
        print("We stopped at {} isbn.".format(last_isbn_tried))
        with open("isbn_temp.txt") as isbn_temp_txt:
            while True:
                isbn_temp_txt.write(raw_txt.readline())


def clean_file():
    print("Hello")
    col_order = ["Author", "Type", "Title", "ISBN", "Year", "Publisher"]
    count = 0  # Index
    with open("isbn.txt", "r") as isbn_txt:
        with open("temp_isbn.txt", "w+") as new_isbn_txt:
            for line in isbn_txt.readlines():
                filtered_line = line.replace("[", "").replace("]", "").replace("\'", "")
                on_correct_col = False
                while not on_correct_col:
                    if not(col_order[count % 6] in filtered_line):
                        filtered_line = "{}:Nah".format(col_order[count % 6])
                        new_isbn_txt.write(filtered_line.strip() + "\n")
                    else:
                        if filtered_line.split(":")[1].strip() == "":
                            filtered_line = "{}:Nah".format(col_order[count % 6])
                        on_correct_col = True
                        new_isbn_txt.write(filtered_line.strip() + "\n")
                        count += 1

        # Continue through the file

# Need to add tester data
# Main file to run is process_isbns()
# The rest (clean_isbn, get_data, and writebook_to_file are helper methods
# fill raw.txt with the isbns that need to be processed, and isbn.txt
# will be filled with the data about the books, or nothing about them


def __str__(self):
    return self.__name__


def __repr__(self):
    return self.__name__


def __format__(self, f):

    if f[-1] == 's':
        return self.__name__
