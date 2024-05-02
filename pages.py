"""Pages module"""
import tkinter as tk
from tkinter import ttk
from controller import *


class Storytelling(ttk.Frame):
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.controller = controller
        self.year = tk.StringVar()
        self.frame = ttk.Frame(self)
        self.init_components()

    def handle_select_year(self, *args):
        self.hist.destroy()
        year = int(self.year.get())

        self.hist = self.controller.handle_select_year(self.frame, year)
        self.hist.grid(row=0, column=0, sticky=tk.NSEW)

    def init_components(self):
        options = {'font': ('Georgia', 21)}
        sticky = {'sticky': tk.NSEW}
        color = {'fg': "Black", 'bg': 'white'}

        #frame = ttk.Frame(self)

        self.hist, self.graph1, self.des_stat = self.controller.initialise(self.frame)
        self.hist.grid(row=0, column=0, **sticky)
        self.graph1.grid(row=0, column=1, **sticky)
        self.des_stat.grid(row=1, column=0, **sticky)

        # combobox
        year_arr = list(map(lambda x: str(x), range(1990, 2020)))

        self.combobox = ttk.Combobox(self, textvariable=self.year, values=year_arr, state='readonly')
        self.combobox.grid(row=2, column=0, columnspan=1, **sticky)

        self.combobox.bind_all('<<ComboboxSelected>>', self.handle_select_year)

        self.year.set('Select Year')

        # frame
        self.frame.grid(row=0, column=0, **sticky)

        for i in range(3):
            self.frame.rowconfigure(i, weight=1)
            self.frame.columnconfigure(i, weight=1)


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
