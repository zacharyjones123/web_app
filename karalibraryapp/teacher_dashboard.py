import tkinter as tk
# import tkinter.ttk as tkk
from website_sql import gui_barcode_test

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
    def __init__(self, parent, controller):
        """
        This initializes the TeacherWindow

        :param parent:
        :param controller:
        """
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

        welcome_lbl = tk.Label(content, text="What do you need today?",
                               anchor=tk.W,
                               justify=tk.LEFT,
                               font='helvetica 20')
        # anchor options: n, ne, e, se, s, sw, w, nw, or center
        welcome_lbl.grid(row=0, column=0)

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

        buttons_frame.grid(row=1, column=0)

        # List box thowing all of the books
        title_header = tk.Label(content, text="Title", font='helvetica 20')
        title_header.grid(row=0, column=1)

        title_listbox = tk.Listbox(content, font='helvetica 20')
        title_listbox.insert(1, "Junebug")
        title_listbox.grid(row=1, column=1)

        author_header = tk.Label(content, text="Author", font='helvetica 20')
        author_header.grid(row=0, column=2)

        author_listbox = tk.Listbox(content, font='helvetica 20')
        author_listbox.insert(1, "Alice Mead")
        author_listbox.grid(row=1, column=2)

        isbn_header = tk.Label(content, text="ISBN", font='helvetica 20')
        isbn_header.grid(row=0, column=3)

        isbn_listbox = tk.Listbox(content, font='helvetica 20')
        isbn_listbox.insert(1, "9780374339647")
        isbn_listbox.grid(row=1, column=3)

        year_header = tk.Label(content, text="Year", font='helvetica 20')
        year_header.grid(row=0, column=4)

        year_listbox = tk.Listbox(content, font='helvetica 20')
        year_listbox.insert(1, "1995")
        year_listbox.grid(row=1, column=4)

        publisher_header = tk.Label(content, text="Publisher", font='helvetica 20')
        publisher_header.grid(row=0, column=5)

        publisher_listbox = tk.Listbox(content, font='helvetica 20')
        publisher_listbox.insert(1, "Macmillan")
        publisher_listbox.grid(row=1, column=5)

        self.columnconfigure(0, weight=1)  # 100%

        self.rowconfigure(0, weight=1)  # 10%
        self.rowconfigure(1, weight=8)  # 80%
        self.rowconfigure(2, weight=1)  # 10%

        def add_book_gui():
            print("This is ran")
            book_data = gui_barcode_test()

            title_listbox.insert(2, book_data["Title"])
            author_listbox.insert(2, book_data["Author"][0])
            isbn_listbox.insert(2, book_data["ISBN"])
            year_listbox.insert(2, book_data["Year"])
            publisher_listbox.insert(2, book_data["Publisher"])

        header.grid(row=0, sticky='news')
        content.grid(row=1, sticky='news')
        footer.grid(row=2, sticky='news')
