import tkinter as tk
# import tkinter.ttk as tkk

"""
LoginWindow

This is the main window for logging in
More information coming soon!
"""
bgimage = None


class LoginWindow(tk.Frame):
    """
    LoginWindow
    """
    @staticmethod
    def init_background_image():
        global bgimage
        fname = "C:\\Users\\Zachary R. Jones\\Downloads\\front_book_PNG.png"
        bgimage = tk.PhotoImage(file=fname)

    def __init__(self, parent, controller):
        """
        This initializes the LoginWindow

        :param parent:
        :param controller:
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.init_background_image()

        content = tk.Frame(self, bg='#D2B48C')  # Tan

        # get the width and height of the image 400x596
        cv = tk.Canvas(content, width=400, height=569)
        cv.pack(expand=tk.YES, fill=tk.BOTH)
        cv.create_image(0, 0, image=bgimage, anchor='nw')

        self.winfo_toplevel().title = "Login"

        login_lbl = tk.Label(content, text="Login", anchor=tk.NW, justify=tk.CENTER, font='helvetica 40', bg="#D2B48C")
        login_lbl.pack()
        cv.create_window(150, 0, anchor=tk.NW, window=login_lbl)

        username_lbl = tk.Label(content, text="Username: ", anchor=tk.W, justify=tk.LEFT, font='helvetica 20', bg='#D2B48C')
        # anchor options: n, ne, e, se, s, sw, w, nw, or center
        username_lbl.pack()
        cv.create_window(0, 100, anchor=tk.NW, window=username_lbl)  # Used this to center vertically

        user_name = tk.StringVar()
        user_name_entry = tk.Entry(content, text="Username: ", textvariable=user_name, font='helvetica 20', bg='#D2B48C')
        user_name_entry.pack()
        cv.create_window(140, 100, anchor=tk.NW, window=user_name_entry)  # Used this to center vertically
        # user_name_entry.grid(row=0, column=1, columnspan=2)

        password_lbl = tk.Label(content, text="Password: ", anchor=tk.W, justify=tk.LEFT, font='helvetica 20', bg='#D2B48C')
        password_lbl.pack()
        cv.create_window(0, 150, anchor=tk.NW, window=password_lbl)  # Used this to center vertically
        # password_lbl.grid(row=1, column=0)

        password = tk.StringVar()
        password_entry = tk.Entry(content, text="Password: ", textvariable=password, font='helvetica 20', bg='#D2B48C')
        password_entry.pack()
        cv.create_window(140, 150, anchor=tk.NW, window=password_entry)  # Used this to center vertically
        # password_entry.grid(row=1, column=1, columnspan=2)

        def login(user, pwd):
            if user == "" and pwd == "":
                return controller.show_frame("TeacherWindow")
            else:
                pass

        login_btn = tk.Button(content, text="Login", command=lambda: login(user_name.get(), password.get()), font=('helvetica 20'))
        login_btn.pack()
        cv.create_window(0, 200, anchor=tk.NW, window=login_btn)  # Used this to center vertically
        # login_btn.grid(row=2, column=0)

        reset_btn = tk.Button(content, text="Reset", font='helvetica 20')
        reset_btn.pack()
        cv.create_window(0, 270, anchor=tk.NW, window=reset_btn)  # Used this to center vertically
        # reset_btn.grid(row=2, column=1)

        new_user_btn = tk.Button(content, text="New User", font='helvetica 20')
        new_user_btn.pack()
        cv.create_window(0, 340, anchor=tk.NW, window=new_user_btn)  # Used this to center vertically
        # new_user_btn.grid(row=2, column=2)

        cv.pack()
        content.grid(row=1, sticky='news')

