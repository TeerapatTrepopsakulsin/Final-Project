"""Pages module"""
import tkinter as tk
from tkinter import ttk
from controller import Controller
from sub_component import Keypad, FilterBar


class Storytelling(ttk.Frame):
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.controller = controller
        self.year = tk.StringVar()
        self.init_components()

    def handle_select_year(self, event: tk.Event):
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 10, 'pady': 5}

        self.hist.destroy()
        self.des_stat.destroy()
        year = int(self.year.get())

        self.hist, self.des_stat = self.controller.handle_select_year(self, year)

        # re-grid
        self.hist.grid(row=2, column=0, columnspan=2, **sticky, **pad)
        self.des_stat.grid(row=3, column=0, columnspan=2, **sticky, **pad)

    def handle_select_graph(self, event: tk.Event):
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 10, 'pady': 5}

        self.graph.destroy()
        graph = event.widget['text']

        self.graph = self.controller.handle_select_graph(self, graph)

        # re-grid
        self.graph.grid(row=0, column=2, rowspan=3, **sticky, **pad)

    def init_components(self):
        options = {'font': ('Arial', 11)}
        sticky = {'sticky': tk.NSEW}
        color = {'fg': "Black", 'bg': 'white'}
        pad = {'padx': 10, 'pady': 5}

        # init graph
        self.hist, self.graph, self.des_stat, graph_arr = self.controller.initialise_stt(self)

        # combobox
        year_arr = list(map(lambda x: str(x), range(1990, 2020)))

        self.combobox = ttk.Combobox(self, textvariable=self.year, values=year_arr, state='readonly')

        self.combobox.bind_all('<<ComboboxSelected>>', self.handle_select_year)

        self.year.set('Select Year')

        # keypad
        self.keypad = Keypad(self, keynames=graph_arr, columns=4)
        self.keypad.configure(height=3, **options)

        self.keypad.bind('<Button>', self.handle_select_graph)

        # label
        self.label = tk.Label(self, text='Annual Death Statistic', anchor='w',  font=("Arial", 14, "bold"))

        # grid
        self.hist.grid(row=2, column=0, columnspan=2, **sticky, **pad)
        self.graph.grid(row=0, column=2, rowspan=3, **sticky, **pad)
        self.des_stat.grid(row=3, column=0, columnspan=2, **sticky, **pad)
        self.combobox.grid(row=1, column=0, **sticky)
        self.keypad.grid(row=3, column=2, **sticky)
        self.label.grid(row=0, column=0, **sticky)

        # frame
        for i in range(2, 3):
            self.rowconfigure(i, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)


class DataExploration(ttk.Frame):
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.controller = controller
        self.year = tk.StringVar()
        self.init_components()

    def handle_generate(self):
        # TODO
        pass

    def init_components(self):
        options = {'font': ('Arial', 11)}
        sticky = {'sticky': tk.NSEW}
        color = {'fg': "Black", 'bg': 'white'}
        pad = {'padx': 10, 'pady': 5}

        # init graph
        self.graph = self.controller.initialise_dte(self)

        # filter bar
        self.filter_bar = FilterBar(self)

        self.filter_bar.bind('<Button>', self.handle_generate)

        # grid
        self.graph.grid(row=0, column=0, **sticky, **pad)
        self.filter_bar.grid(row=0, column=1, **sticky, **pad)

        # frame
        for i in range(1):
            self.rowconfigure(i, weight=1)
        for i in range(2):
            self.columnconfigure(i, weight=1)


if __name__ == '__main__':
    import main
