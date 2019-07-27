import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from isbn_processor import get_book_list_from_file
from isbn_processor import add_book
from isbn_processor import process_isbns
"""
The purpose of this is to take
the dictionary from the
isbn_processor.py and perform
basic filtering and statistics
"""


def make_horizontal_bar_graph(x_axis, y_axis, x_label, title):
    y_pos = np.arange(len(x_axis))

    plt.barh(y_pos, y_axis, align='center', alpha=0.5)
    plt.yticks(y_pos, x_axis)
    plt.xlabel(x_label)
    plt.title(title)

    plt.show()


def count_books():
    with open("isbn.txt", "r") as isbn:
        count = 0
        for line in isbn.readlines():
            if "Type" in line:
                count += 1
        print("Num Of Books: {}".format(count))


def collect_authors():
    authors = {}
    with open("isbn.txt", "r") as isbn:
        count = 0
        for line in isbn.readlines():
            if "Author" in line:
                line_split = line.split(":")
                if line_split[1] in authors.keys():
                    authors[line_split[1]] += 1
                else:
                    authors[line_split[1]] = 1
    for i, j in authors.items():
        print("{}:{}".format(i.strip(), j))


def collect_isbns():
    isbns = []
    with open("isbn.txt", "r") as isbn:
        for line in isbn.readlines():
            if "ISBN" in line:
                line_split = line.split(":")
                isbns.append(line_split[1].strip())
    print(isbns)


def collect_years():
    years = {}
    with open("isbn.txt", "r") as isbn:
        for line in isbn.readlines():
            if "Year" in line:
                line_split = line.split(":")
                if line_split[1] in years.keys():
                    years[line_split[1]] += 1
                else:
                    years[line_split[1]] = 1
    x_axis = []
    y_axis = []
    for i in sorted(years.keys()):
        if i.strip().isnumeric():
            x_axis.append(i.strip())
            y_axis.append(years[i])
    make_horizontal_bar_graph(x_axis, y_axis, "Amount of Books", "Years For Books")


collect_isbns()

# add_book("978-0679824114")

# book_dict = get_dict_from_file()
# print(book_dict)

# process_isbns()
