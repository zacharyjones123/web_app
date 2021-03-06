import tkinter as tk
# import tkinter.ttk as tkk

"""
NewUserWindow

Used to get info about a new user!
More information coming soon!
"""


class NewUserWindow(tk.Frame):
    """
    NewUserWindow
    """

    def __init__(self, parent, controller):
        """
        This initializes the NewUserWindow

        :param parent:
        :param controller:
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.winfo_toplevel().title = "New User"

        header = tk.Frame(self)
        firstname_lbl = tk.Label(header, text="Firstname: ", justify=tk.LEFT, font='helvetica 20')
        firstname_lbl.grid(row=0, column=0)

        firstname_entry = tk.Entry(header, font='helvetica 20')
        firstname_entry.grid(row=0, column=1)

        lastname_lbl = tk.Label(header, text="Lastname: ", justify=tk.LEFT, font='helvetica 20')
        lastname_lbl.grid(row=1, column=0)

        lastname_entry = tk.Entry(header, font='helvetica 20')
        lastname_entry.grid(row=1, column=1)

        username_lbl = tk.Label(header, text="Username: ", justify=tk.LEFT, font='helvetica 20')
        username_lbl.grid(row=3, column=0)

        username_entry = tk.Entry(header, font='helvetica 20')
        username_entry.grid(row=3, column=1)

        submit_btn = tk.Button(header, text="Submit", font='helvetica 20')
        submit_btn.grid(row=4, column=0, columnspan=2)

        reset_btn = tk.Button(header, text="Reset", font='helvetica 20')
        reset_btn.grid(row=5, column=0, columnspan=2)

        header.pack()
