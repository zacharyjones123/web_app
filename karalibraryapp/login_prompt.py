import tkinter as tk
# import tkinter.ttk as tkk


class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.winfo_toplevel().title = "Login"

        name = "Kara"
        username_lbl = tk.Label(self, text="Username: ".format(name), anchor=tk.W, justify=tk.LEFT, font=('helvetica 20'))
        username_lbl.grid(row=0, column=0)

        user_name = tk.StringVar()
        user_name_entry = tk.Entry(self, text="Username: ", textvariable=user_name, font=('helvetica 20'))
        user_name_entry.grid(row=0, column=1, columnspan=2)

        password_lbl = tk.Label(self, text="Password: ".format(name), anchor=tk.W, justify=tk.LEFT, font=('helvetica 20'))
        password_lbl.grid(row=1, column=0)

        password = tk.StringVar()
        password_entry = tk.Entry(self, text="Password: ", textvariable=password, font=('helvetica 20'))
        password_entry.grid(row=1, column=1, columnspan=2)

        def login(user, pwd):
            if user == "" and pwd == "":
                return controller.show_frame("TeacherWindow")
            else:
                pass

        login_btn = tk.Button(self, text="Login", command=lambda: login(user_name.get(), password.get()), font=('helvetica 20'))
        login_btn.grid(row=2, column=0)

        reset_btn = tk.Button(self, text="Reset", font='helvetica 20')
        reset_btn.grid(row=2, column=1)

        new_user_btn = tk.Button(self, text="New User", font='helvetica 20')
        new_user_btn.grid(row=2, column=2)

