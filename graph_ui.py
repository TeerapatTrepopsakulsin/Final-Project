import graph_generator
import math
import tkinter as tk
from tkinter import ttk, scrolledtext
from winsound import MessageBeep, SND_NOWAIT


class GraphUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graph")
        self.init_components()

    def handle_event(self, event: tk.Event):
        pass

    def init_components(self):
        """Create components and layout the UI."""
        # notebook

        # graph_left
        # label_stat
        # graph_right
        # selection

        # graph
        # filter_table

        # fill the window

        pass

    def run(self):
        """start the app, wait for events"""
        self.mainloop()
