"""Controller module."""
import tkinter as tk
from tkinter import ttk
from graph_generator import GraphGenerator, DefaultGraph


class Controller:
    def __init__(self, graph_generator: GraphGenerator):
        self.display = DefaultGraph()
        self.generator = graph_generator

    def initialise(self, frame: ttk.Frame):
        # initialise the generator
        self.generator.start_year = 2019
        self.generator.end_year = 2019
        self.generator.set_only_country()

        self.generator.graph = 'Histogram'
        generator = self.generator.get_generator()
        hist = generator.generate(frame)

        self.generator.graph = 'Stat'
        generator = self.generator.get_generator()
        des_stat = generator.generate(frame)

        graph = self.display.graph2(frame)

        return hist, graph, des_stat

    def handle_select_year(self, frame: ttk.Frame, year):
        self.generator.start_year = year
        self.generator.end_year = year
        self.generator.set_only_country()

        self.generator.graph = 'Histogram'
        generator = self.generator.get_generator()
        hist = generator.generate(frame)

        self.generator.graph = 'Stat'
        generator = self.generator.get_generator()
        des_stat = generator.generate(frame)

        return hist, des_stat

    def handle_select_graph(self, frame: ttk.Frame, graph):
        to_func = {'Speed limits/Death rate': lambda x: self.display.graph2(x),
                   'Speed limits (Rural)/Death rate': lambda x: self.display.graph2_rural(x),
                   'Speed limits (Urban)/Death rate': lambda x: self.display.graph2_urban(x),
                   'Seat-belt law/Death rate': lambda x: self.display.graph1(x),
                   'Ages (Pie chart)': lambda x: self.display.graph3(x),
                   'Types (Pie chart)': lambda x: self.display.graph4(x),
                   'Ages (Bar graph)': lambda x: self.display.graph5(x),
                   'Types (Bar graph)': lambda x: self.display.graph6(x)
                   }

        func = to_func[graph]
        graph = func(frame)

        return graph


if __name__ == '__main__':
    import main
