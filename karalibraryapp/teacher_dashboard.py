import tkinter as tk
# import tkinter.ttk as tkk
from karalibraryapp.website_sql import gui_barcode_test
from karalibraryapp.website_sql import select_from_database

"""
TeacherWindow
"""


def create_menu(window):
    """
    This is used to create the menu for the window

    :param window:
    :return:
    """

    # This makes the menu
    # --------------------------------------------------
    menubar = tk.Menu(window)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut")
    editmenu.add_command(label="Copy")
    editmenu.add_command(label="Paste")
    menubar.add_cascade(label="Edit", menu=editmenu)

    bookmenu = tk.Menu(menubar, tearoff=0)
    bookmenu.add_command(label="Add Book")
    bookmenu.add_command(label="Edit Book")
    bookmenu.add_command(label="List Book")
    menubar.add_cascade(label="Books", menu=bookmenu)

    studentmenu = tk.Menu(menubar, tearoff=0)
    studentmenu.add_command(label="Add Student")
    studentmenu.add_command(label="Edit Student")
    studentmenu.add_command(label="List Students")
    menubar.add_cascade(label="Students", menu=studentmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About")
    menubar.add_cascade(label="Help", menu=helpmenu)

    # --------------------------------------------------

    # This is the part about the right click feature
    # ----------------------------------------------
    def popup(event):
        menubar.post(event.x_root, event.y_root)

    window.bind("<Button-3>", popup)
    # ----------------------------------------------

    # display the menu
    window.config(menu=menubar)


class TeacherWindow(tk.Frame):
    """
    TeacherWindow
    """

    @staticmethod
    def init_background_image():
        global bgimage
        fname = "C:\\Users\\Zachary R. Jones\\Downloads\\open_book_PNG.png"
        bgimage = tk.PhotoImage(file=fname)

    def __init__(self, parent, controller):
        """
        This initializes the TeacherWindow

        :param parent:
        :param controller:
        """

        self.init_background_image()

        tk.Frame.__init__(self, parent)
        self.controller = controller

        header = tk.Frame(self, bg='black')
        content = tk.Frame(self, bg='red')
        footer = tk.Frame(self, bg='black')

        name = "Kara"
        title_lbl = tk.Label(header, text="Welcome {},".format(name), anchor=tk.W, justify=tk.LEFT, font='helvetica 32')
        title_lbl.pack(side=tk.LEFT)

        logout_btn = tk.Button(header,
                               text="Log Off", anchor=tk.E,
                               command=lambda: controller.show_frame("LoginWindow"),
                               justify=tk.RIGHT, font='helvetica 32')
        logout_btn.pack(side=tk.RIGHT)

        # get the width and height of the image 400x596
        cv = tk.Canvas(content, width=800, height=656)
        cv.pack(expand=tk.YES, fill=tk.BOTH)
        cv.create_image(0, 0, image=bgimage, anchor='nw')

        welcome_lbl = tk.Label(content, text="What do you need today?",
                               anchor=tk.W,
                               justify=tk.LEFT,
                               font='helvetica 20')
        # anchor options: n, ne, e, se, s, sw, w, nw, or center
        welcome_lbl.pack()
        cv.create_window(0, 0, anchor=tk.NW, window=welcome_lbl)

        # New Frame for the buttons
        buttons_frame = tk.Frame(content, bg="black")
        # Now need to add buttons
        # View Books Button
        view_books_btn = tk.Button(buttons_frame,
                                   text="View Books",
                                   command=lambda: add_book_gui(),
                                   font='helvetica 20')
        view_books_btn.grid(row=0, column=0)

        # Stats Button
        stats_btn = tk.Button(buttons_frame, text="Statistics", font='helvetica 20')
        stats_btn.grid(row=1, column=0)

        # View Students Button
        view_students_btn = tk.Button(buttons_frame, text="View Students", font='helvetica 20')
        view_students_btn.grid(row=2, column=0)

        # Add Books Button
        add_book_btn = tk.Button(buttons_frame, text="Add Book", font='helvetica 20')
        add_book_btn.grid(row=3, column=0)

        # Edit Book Button
        edit_book_btn = tk.Button(buttons_frame, text="Edit Book", font='helvetica 20')
        edit_book_btn.grid(row=4, column=0)

        # New Feature 1
        new_1_btn = tk.Button(buttons_frame, text="New Feature 1", font='helvetica 20')
        new_1_btn.grid(row=5, column=0)

        # New Feature 2
        new_2_btn = tk.Button(buttons_frame, text="New Feature 2", font='helvetica 20')
        new_2_btn.grid(row=6, column=0)

        # New Feature 3
        new_3_btn = tk.Button(buttons_frame, text="New Feature 3", font='helvetica 20')
        new_3_btn.grid(row=7, column=0)


        buttons_frame.pack()
        cv.create_window(0, 50, anchor=tk.NW, window=buttons_frame)

        # List box thowing all of the books
        # New Frame for the books
        books_frame = tk.Frame(content, bg="black")
        title_header = tk.Label(books_frame, text="Books", font='helvetica 15', width=50)
        title_header.pack(fill=tk.Y)

        title_scrollbar = tk.Scrollbar(books_frame, orient=tk.VERTICAL, width=50)
        title_listbox = tk.Listbox(books_frame, font='helvetica 15', yscrollcommand=title_scrollbar.set, width=100)

        # Add a book
        self.add_all_database_books(title_listbox)
        # itle_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        title_listbox.pack(fill=tk.Y)

        books_frame.pack()
        cv.create_window(200, 50, anchor=tk.NW, window=books_frame)
        cv.pack()

        self.columnconfigure(0, weight=1)  # 100%

        self.rowconfigure(0, weight=1)  # 10%
        self.rowconfigure(1, weight=8)  # 80%
        self.rowconfigure(2, weight=1)  # 10%

        def add_book_gui():
            print("This is ran")
            book_data = gui_barcode_test()

            title_listbox.insert(2, book_data["Title"])
            # author_listbox.insert(2, book_data["Author"][0])
            # isbn_listbox.insert(2, book_data["ISBN"])
            # year_listbox.insert(2, book_data["Year"])
            # publisher_listbox.insert(2, book_data["Publisher"])

        header.grid(row=0, sticky='news')
        content.grid(row=1, sticky='news')
        footer.grid(row=2, sticky='news')

    def add_book_GUI(self, listbox, newbookstring):
        print("Add A new book")
        listbox.insert(1, newbookstring)

    def add_all_database_books(self, listbox):
        result_set = select_from_database()
        for result in result_set:
            listbox.insert(1, result)
