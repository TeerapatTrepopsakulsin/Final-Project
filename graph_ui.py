import graph_generator
from pages import *
import tkinter as tk
from tkinter import ttk, scrolledtext
from winsound import MessageBeep, SND_NOWAIT


class GraphUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graph")
        #self.geometry('1280x720')
        self.init_components()

    def handle_event(self, event: tk.Event):
        pass

    def init_components(self):
        """Create components and layout the UI."""
        sticky = {'sticky': tk.NSEW}
        # notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, **sticky)

        ## create frames
        frame1 = Storytelling(self.notebook, width=1280, height=720)
        frame2 = DataExploration(self.notebook, width=1280, height=720)


        frame1.grid(row=0, column=0, **sticky)
        frame2.grid(row=0, column=0, **sticky)

        ## add frames to notebook
        self.notebook.add(frame1, text='Storytelling')
        self.notebook.add(frame2, text='Data Exploration')

        # graph_left
        # label_stat
        # graph_right
        # selection

        # graph
        # filter_table

        # fill the window
        for row in range(5):
            self.rowconfigure(row, weight=1)
        for col in range(3):
            self.columnconfigure(col, weight=1)

    def run(self):
        """start the app, wait for events"""
        self.mainloop()


if __name__ == '__main__':
    import main
