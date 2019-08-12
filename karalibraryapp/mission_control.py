import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from start_prompt import StartWindow
from login_prompt import LoginWindow
from teacher_dashboard import TeacherWindow
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

"""
MissionControl

This class serves as the way that
all of the windows are organized and 
switched between to share data
"""


class SampleApp(tk.Tk):
    """
    MissionControl
    """

    def __init__(self, *args, **kwargs):
        """
        This initializes the MissionControl
        :param args:
        :param kwargs:
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("1900x600")
        self.wm_title("Kara's Library Application")

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
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    """
    Main method to be ran
    """

    app = SampleApp()
    app.mainloop()
