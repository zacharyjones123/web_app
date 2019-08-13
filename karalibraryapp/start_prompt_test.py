import tkinter as tk  # python 3

from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

"""
StartWindow

This window is where the program starts
More information coming soon!
"""

bgimage = None


class Mission(tk.Tk):
    """
     MissionControl
     """

    @staticmethod
    def init_background_image():
        global bgimage
        fname = "C:\\Users\\Zachary R. Jones\\Downloads\\front_book_PNG.png"
        bgimage = tk.PhotoImage(file=fname)

    def __init__(self, *args, **kwargs):
        """
        This initializes the MissionControl
        :param args:
        :param kwargs:
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.init_background_image()
        self.geometry("{}x{}".format(str(bgimage.width()), str(bgimage.height())))
        self.wm_title("Library Application")
        # self.overrideredirect(1) # This is used to get rid of title bar

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartWindow,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartWindow")

    def show_frame(self, page_name):
        """
        This shows whatever frame is given on the
        main root frame

        :param page_name:
        :return:
        """
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartWindow(tk.Frame):

    """
    TeacherWindow
    """
    def __init__(self, parent, controller):
        global bgimage
        """
        This initializes the TeacherWindow

        :param parent:
        :param controller:
        """
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
                                command=self.quit) # flat, groove, raised, ridge, solid, or sunken
        # anchor options: n, ne, e, se, s, sw, w, nw, or center
        cv.create_window(150, 300, anchor = tk.NW, window=welcome_lbl) # Used this to center vertically

        cv.pack()

        self.columnconfigure(0, weight=1)  # 100%

        self.rowconfigure(0, weight=1)  # 10%
        self.rowconfigure(1, weight=8)  # 80%
        self.rowconfigure(2, weight=1)  # 10%

        content.grid(row=1, sticky='news')


if __name__ == "__main__":
    """
    Main method to be ran
    """

    app = Mission()
    app.mainloop()
