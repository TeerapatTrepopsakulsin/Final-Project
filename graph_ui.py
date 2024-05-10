"""Main UI module for application."""
import tkinter as tk
from tkinter import ttk
from controller import Controller
from pages import Storytelling, DataExploration, Dataset


class GraphUI(tk.Tk):
    """UI class"""
    def __init__(self, controller: Controller):
        super().__init__()
        self.title("Road incident deaths")
        self.controller = controller
        self.init_components()

    def init_components(self):
        """Create components and layout the UI."""
        sticky = {'sticky': tk.NSEW}

        # menubar
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=False)
        file_menu.add_command(label='Exit', command=self.destroy)
        self.menu.add_cascade(label="File", menu=file_menu)

        # notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, **sticky)

        # create frames
        frame1 = Storytelling(self.notebook, self.controller)
        frame2 = DataExploration(self.notebook, self.controller)
        frame3 = Dataset(self.notebook, self.controller)

        frame1.grid(row=0, column=0, **sticky)
        frame2.grid(row=0, column=0, **sticky)
        frame3.grid(row=0, column=0, **sticky)

        # add frames to notebook
        self.notebook.add(frame1, text='Storytelling')
        self.notebook.add(frame2, text='Data Exploration')
        self.notebook.add(frame3, text='Dataset')

        # fill the window
        for row in range(1):
            self.rowconfigure(row, weight=1)
        for col in range(1):
            self.columnconfigure(col, weight=1)

    def run(self):
        """start the app, wait for events"""
        self.mainloop()
