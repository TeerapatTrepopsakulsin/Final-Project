"""Controller module."""
import tkinter as tk
from tkinter import ttk
from graph_generator import GraphGenerator, DefaultGraph


class Controller:
    def __init__(self, graph_generator: GraphGenerator):
        self.display = DefaultGraph()
        self.generator = graph_generator

    def initialise_stt(self, frame: ttk.Frame):
        # initialise the generator
        self.generator.setup(start_year=2019, end_year=2019, unit='death_rate', array=['death_rate'], mode='standard')
        self.generator.set_only_country()

        # generating
        size = (4, 4)
        self.generator.setup(graph='Histogram')
        generator = self.generator.get_generator()
        hist = generator.generate(frame, size)

        self.generator.setup(graph='Stat')
        generator = self.generator.get_generator()
        des_stat = generator.generate(frame, size)

        size = (5, 4)
        graph = self.display.graph2(frame, size)

        return hist, graph, des_stat

    def handle_select_year(self, frame: ttk.Frame, year):
        # initialise the generator
        self.generator.setup(start_year=year, end_year=year, unit='death_rate', array=['death_rate'], mode='standard')
        self.generator.set_only_country()

        # generating
        size = (4, 4)

        self.generator.setup(graph='Histogram')
        generator = self.generator.get_generator()
        hist = generator.generate(frame, size)

        self.generator.setup(graph='Stat')
        generator = self.generator.get_generator()
        des_stat = generator.generate(frame, size)

        return hist, des_stat

    def handle_select_graph(self, frame: ttk.Frame, graph):
        to_func = {'Speed limits/Death rate': self.display.graph2,
                   'Speed limits (Rural)/Death rate': self.display.graph2_rural,
                   'Speed limits (Urban)/Death rate': self.display.graph2_urban,
                   'Seat-belt law/Death rate': self.display.graph1,
                   'Ages (Pie chart)': self.display.graph3,
                   'Types (Pie chart)': self.display.graph4,
                   'Ages (Bar graph)': self.display.graph5,
                   'Types (Bar graph)': self.display.graph6
                   }

        func = to_func[graph]
        size = (5, 3)
        graph = func(frame, size)

        return graph

    def initialise_dte(self, frame: ttk.Frame):
        # TODO
        return tk.Canvas(frame, background='black')

    def handle_generate(self):
        # TODO
        # if len(self.generator.array) >= 5:
        #     self.generator.array = [self.generator.unit]
        pass


if __name__ == '__main__':
    import main
