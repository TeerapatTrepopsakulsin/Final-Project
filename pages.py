"""Pages module for each page in the UI."""
import copy
import tkinter as tk
from tkinter import ttk
from controller import Controller
from sub_component import Keypad, FilterBar


class Storytelling(ttk.Frame):
    """Storytelling page where users can view graphs and statistics."""
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.controller = copy.deepcopy(controller)
        self.year = tk.StringVar()
        self.init_components()

    def handle_select_year(self, *args):
        """
        Change the histogram and descriptive statistics after users select year.
        """
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
        """
        Change the graph after users select which graph to view.
        """
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 10, 'pady': 5}

        self.graph.destroy()
        graph = event.widget['text']

        self.graph = self.controller.handle_select_graph(self, graph)

        # re-grid
        self.graph.grid(row=0, column=2, rowspan=3, **sticky, **pad)

    def init_components(self):
        """
        Initialise the components and layout for the page UI.
        """
        options = {'font': ('Arial', 11)}
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 10, 'pady': 5}

        # init graph
        self.hist, self.graph, self.des_stat, graph_arr = self.controller.initialise_stt(self)

        # combobox
        year_arr = list(map(str, range(1990, 2020)))

        self.combobox = ttk.Combobox(self, textvariable=self.year,
                                     values=year_arr, state='readonly')

        self.combobox.bind('<<ComboboxSelected>>', self.handle_select_year)

        self.year.set('Select Year')

        # keypad
        self.keypad = Keypad(self, keynames=graph_arr, columns=4)
        self.keypad.configure(height=3, **options)

        self.keypad.bind('<Button>', self.handle_select_graph)

        # label
        self.label = tk.Label(self, text='Annual Death Statistic',
                              anchor='w',  font=("Arial", 14, "bold"))

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
        self.columnconfigure(2, weight=3)


class DataExploration(ttk.Frame):
    """Data Exploration page where users can alter parameter values,
    filter data, or manipulate the view.
    """
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.controller = copy.deepcopy(controller)
        self.init_components()

    def handle_generate(self, *args):
        """
        Change the graph to the new filtered graph according to the users
        after pressed Generate.
        """
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 10, 'pady': 5}

        self.graph.destroy()
        self.graph = self.controller.handle_generate(self)

        # re-grid
        self.graph.grid(row=0, column=0, **sticky, **pad)

    def init_components(self):
        """
        Initialise the components and layout for the page UI.
        """
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 10, 'pady': 5}

        # init graph
        self.graph = self.controller.initialise_dte(self)

        # filter bar
        self.filter_bar = FilterBar(self, self.controller)

        # grid
        self.graph.grid(row=0, column=0, **sticky, **pad)
        self.filter_bar.grid(row=0, column=1, **sticky, **pad)

        # frame
        for i in range(1):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)


class Dataset(ttk.Frame):
    """Dataset page where users can view dataset."""
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.controller = copy.deepcopy(controller)
        self.init_components()

    def init_components(self):
        """
        Initialise the components and layout for the page UI.
        """
        sticky = {'sticky': tk.NSEW}

        # treeview
        self.treeview = self.controller.get_dataset_treeview(self)

        # scrollbar
        self.y_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=self.y_scrollbar.set)
        self.x_scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.treeview.xview)
        self.treeview.configure(xscroll=self.x_scrollbar.set)

        # grid
        self.treeview.grid(row=0, column=0, **sticky)
        self.y_scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.x_scrollbar.grid(row=1, column=0, sticky=tk.EW)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
