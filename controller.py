"""Controller module."""
import tkinter as tk
from tkinter import ttk
from graph_generator import GraphGenerator, DefaultGraph


class Controller:
    def __init__(self, graph_generator: GraphGenerator):
        self.generator = graph_generator
        self.display = None

    def initialise(self, frame: ttk.Frame):
        self.display = DefaultGraph(frame)

        self.generator.graph = 'Histogram'
        self.histgen = self.generator.get_generator(frame)

        hist = self.histgen.generate()

        graph1 = self.display.graph1()

        des_stat = self.display.stat()

        return hist, graph1, des_stat

    def handle_select_year(self, frame: ttk.Frame, year):
        self.generator.graph = 'Histogram'
        self.generator.start_year = year
        self.generator.end_year = year
        self.histgen = self.generator.get_generator(frame)
        hist = self.histgen.generate()
        return hist
