import tkinter as tk                # python 3
# from tkinter import font  as tkfont # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

"""
StartWindow

This window is where the program starts
More information coming soon!
"""
bgimage = None


class StartWindow(tk.Frame):
    """
    TeacherWindow
    """

    @staticmethod
    def init_background_image():
        global bgimage
        fname = "C:\\Users\\Zachary R. Jones\\Downloads\\front_book_PNG.png"
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

        content = tk.Frame(self, bg='#D2B48C')# Tan

        # get the width and height of the image 400x596
        cv = tk.Canvas(content, width=400, height=569)
        cv.pack(expand=tk.YES, fill=tk.BOTH)
        cv.create_image(0, 0, image=bgimage, anchor='nw')

        title_lbl = tk.Label(content,
                             text="Library Application",
                             anchor=tk.CENTER,
                             justify=tk.CENTER,
                             font='helvetica 30',
                             bg="#D2B48C"
                             )
        title_lbl.pack() # used this to center vertically
        cv.create_window(55, 100, anchor = tk.NW, window=title_lbl)

        welcome_lbl = tk.Button(content, text="Enter",
                                anchor=tk.CENTER,
                                justify=tk.CENTER,
                                font='helvetica 30',
                                relief = "groove",
                                bg="#D2B48C",
                                command=lambda: controller.show_frame("LoginWindow")) # flat, groove, raised, ridge, solid, or sunken
        # anchor options: n, ne, e, se, s, sw, w, nw, or center
        cv.create_window(150, 300, anchor = tk.NW, window=welcome_lbl) # Used this to center vertically

        cv.pack()

        self.columnconfigure(0, weight=1)  # 100%

        self.rowconfigure(0, weight=1)  # 10%
        self.rowconfigure(1, weight=8)  # 80%
        self.rowconfigure(2, weight=1)  # 10%

        content.grid(row=1, sticky='news')
