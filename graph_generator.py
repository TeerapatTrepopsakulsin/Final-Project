import sys
import os
import copy
import inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from enum import Enum


class GraphGenerator:
    def __init__(self):
        self.__start_year = 1990
        self.__end_year = 2019

    def generate(self):
        pass

    @property
    def start_year(self):
        return self.__start_year

    @start_year.setter
    def start_year(self, year):
        self.__start_year = year

    @property
    def end_year(self):
        return self.__end_year

    @end_year.setter
    def end_year(self, year):
        self.__end_year = year


class LinegraphGenerator(GraphGenerator):
    pass


class HistogramGenerator(GraphGenerator):
    pass


class BargraphGenerator(GraphGenerator):
    pass


class DataframeGenerator:
    pass


class DefaultGraph(Enum):
    pass
