import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from karalibraryapp.start_prompt import StartWindow
from karalibraryapp.login_prompt import LoginWindow
from karalibraryapp.teacher_dashboard import TeacherWindow
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

"""
MissionControl

This class serves as the way that
all of the windows are organized and 
switched between to share data
"""

bgimage = None


class SampleApp(tk.Tk):
    """
    MissionControl
    """

    @staticmethod
    def init_background_image(self, fname):
        global bgimage
        bgimage = tk.PhotoImage(file=fname)
        self.geometry("{}x{}".format(str(bgimage.width()), str(bgimage.height())))

    def __init__(self, *args, **kwargs):
        """
        This initializes the MissionControl
        :param args:
        :param kwargs:
        """
        tk.Tk.__init__(self, *args, **kwargs)

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
        for F in (StartWindow, LoginWindow, TeacherWindow):
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
        start_bg = "C:\\Users\\Zachary R. Jones\\Downloads\\front_book_PNG.png"
        login_bg = "C:\\Users\\Zachary R. Jones\\Downloads\\front_book_PNG.png"
        teacher_bg = "C:\\Users\\Zachary R. Jones\\Downloads\\open_book_PNG.png"

        '''Show a frame for the given page name'''
        if page_name == "StartWindow":
            self.init_background_image(self, start_bg)
            self.geometry("{}x{}".format(str(bgimage.width()), str(bgimage.height())))
            self.wm_title("StartWindow")
        elif page_name == "LoginWindow":
            self.init_background_image(self, login_bg)
            self.geometry("{}x{}".format(str(bgimage.width()), str(bgimage.height())))
            self.wm_title("LoginWindow")
        elif page_name == "TeacherWindow":
            self.init_background_image(self, teacher_bg)
            self.geometry("{}x{}".format(str(bgimage.width()), str(bgimage.height())))
            self.wm_title("TeacherWindow")
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    """
    Main method to be ran
    """

    app = SampleApp()
    app.mainloop()
