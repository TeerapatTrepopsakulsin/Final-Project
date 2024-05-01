"""Pages module"""
import tkinter as tk
from tkinter import ttk
from graph_generator import *


class Storytelling(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.init_components()

    def init_components(self):
        options = {'font': ('Georgia', 21)}
        sticky = {'sticky': tk.NSEW}
        color = {'fg': "Black", 'bg': 'white'}

        frame = ttk.Frame(self)
        ########################
        graph1 = DefaultGraph.graph1(frame)
        graph1.grid(row=1, column=1, **sticky)

        plot = DefaultGraph.plot(frame)
        plot.grid(row=1, column=2, **sticky)

        des_stat = DefaultGraph.stat(frame)
        des_stat.grid(row=2, column=1, **sticky)
        ##########################

        frame.grid(row=0, column=0, **sticky)

        for i in range(5):
            frame.rowconfigure(i, weight=1)
            frame.columnconfigure(i, weight=1)


class DataExploration(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.init_components()

    def init_components(self):
        options = {'font': ('Georgia', 21)}
        sticky = {'sticky': tk.NSEW}
        color = {'fg': "Black", 'bg': 'white'}

        frame = ttk.Frame(self)

        self.label = tk.Label(frame, text='In progress...', **options, **color)
        self.label.grid(row=1, column=1, **sticky)

        frame.grid(row=0, column=0, **sticky)

        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(1, weight=1)


if __name__ == '__main__':
    import main
