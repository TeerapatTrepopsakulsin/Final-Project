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
        self.generator.graph = 'Histogram'
        self.generator.start_year = 2019
        self.generator.end_year = 2019
        generator = self.generator.get_generator()

        hist = generator.generate(frame)

        graph1 = self.display.graph2(frame)

        des_stat = self.display.stat(frame)

        return hist, graph1, des_stat

    def handle_select_year(self, frame: ttk.Frame, year):
        self.generator.graph = 'Histogram'
        self.generator.start_year = year
        self.generator.end_year = year
        self.histgen = self.generator.get_generator()
        hist = self.histgen.generate(frame)
        return hist


if __name__ == '__main__':
    import main
