"""Controller module."""
import tkinter as tk
from tkinter import ttk
from graph_generator import GraphGenerator, DefaultGraphCatalog


class Controller:
    def __init__(self, graph_generator: GraphGenerator, default_graph: type[DefaultGraphCatalog]):
        self.catalog = default_graph
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
        graph = self.catalog.get_func('Speed limits/Death rate')(frame, size)

        default_graph_list = [i.value['label'] for i in DefaultGraphCatalog]

        return hist, graph, des_stat, default_graph_list

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
        func = self.catalog.get_func(graph)
        size = (5, 3)
        _graph = func(frame, size)

        return _graph

    def initialise_dte(self, frame: ttk.Frame):
        # initialise the generator
        self.generator.setup(start_year=1990, end_year=2019, entity1='World', entity2='Thailand',
                             unit='death_rate', array=['death_rate'], mode='standard')
        self.generator.set_all()

        size = (8, 5)
        self.generator.graph = 'Line Graph'
        generator = self.generator.get_generator()
        line = generator.generate(frame, size)

        # TODO

        return line

    def handle_generate(self):
        # TODO
        # if len(self.generator.array) >= 5:
        #     self.generator.array = [self.generator.unit]
        pass


if __name__ == '__main__':
    import main
