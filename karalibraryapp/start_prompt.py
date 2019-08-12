import tkinter as tk                # python 3
# from tkinter import font  as tkfont # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

"""
StartWindow

This window is where the program starts
More information coming soon!
"""


class StartWindow(tk.Frame):
    """
    StartWindow
    """

    def __init__(self, parent, controller):
        """
        This initializes the StartWindow

        :param parent:
        :param controller:
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        welcome_message_lbl = tk.Label(self, text="Kara Library Application", justify=tk.CENTER, font='helvetica 20')
        welcome_message_lbl.grid(row=0, column=0)

        enter_btn = tk.Button(self, text="Enter",
                              command=lambda: controller.show_frame("LoginWindow"),
                              justify=tk.CENTER, font='helvetica 20')
        enter_btn.grid(row=1, column=0)
