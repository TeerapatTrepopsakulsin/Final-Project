import sys
import os
import copy
from tkinter import ttk
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum
from abc import ABC

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


DF = pd.read_csv("data.csv")
DF_OC = pd.read_csv("data_only_country.csv")


class GraphGenerator(ABC):
    def __init__(self):
        self.__start_year = 1990
        self.__end_year = 2019
        self.__entity = 'World'
        self.__type_or_age = 'age'
        self.__unit = 'death_total'
        self.__mode = 'Standard'
        self.__graph = 'Histogram'

    def get_generator(self, frame: ttk.Frame) -> 'GraphGenerator':
        attr = copy.copy(self.__dict__)
        if self.graph == 'Line Graph':
            return LinegraphGenerator()
        elif self.graph == 'Histogram':
            return HistogramGenerator(frame, **attr)
        elif self.graph == 'Bar graph':
            return LinegraphGenerator()

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

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph):
        self.__graph = graph

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self.__unit = unit


class LinegraphGenerator(GraphGenerator):
    pass


class BargraphGenerator(GraphGenerator):
    pass


class HistogramGenerator(GraphGenerator):
    def __init__(self, frame: ttk.Frame, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
        self.frame = frame

    def generate(self):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # histogram
        g7_df = DF_OC[(DF_OC['Year'] >= self.start_year) & (DF_OC['Year'] <= self.end_year)]
        hist = g7_df['death_rate'].hist(bins=20)
        plt.title('Histogram for death rate')
        plt.xlabel('Death rate (deaths per 100,000 people)')
        plt.ylabel('Frequency')

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()

        return canvas.get_tk_widget()


class DataframeGenerator:
    pass


class DefaultGraph:
    def __init__(self):
        pass

    def graph1(self, frame: ttk.Frame):
        # figure
        fig = plt.figure()

        # bar graph
        g1_df = DF_OC.groupby(['seatbelt_law'])['death_rate'].mean()

        colour = np.array(['red', 'green'])

        g1_df.plot(kind='bar', stacked=False, xlabel='Existence of seat-belt law',
                   ylabel='Average death rate (deaths per 100,000 people)', color=colour, rot=0)
        plt.title('Average death rate of countries with and without seat-belt law')

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    @staticmethod
    def graph2_setup():
        g2_df = DF_OC.groupby(['Entity'])[['death_rate', 'rural_speed_limit', 'urban_speed_limit']].mean()

        a = g2_df['rural_speed_limit']
        b = g2_df['death_rate']
        c = g2_df['urban_speed_limit']

        return a, b, c

    def graph2(self, frame: ttk.Frame):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # scatter chart
        rural, death_rate, urban = self.graph2_setup()

        plt.scatter(rural, death_rate, c='red')
        plt.scatter(urban, death_rate, c='blue')
        plt.title('Correlation between death rate and speed limits')
        plt.xlabel('Speed limit (km/h)')
        plt.ylabel('Average death rate (deaths per 100,000 people)')
        plt.legend(['rural', 'urban'])

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    def graph2_rural(self, frame: ttk.Frame):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # scatter chart
        rural, death_rate, urban = self.graph2_setup()

        plt.scatter(rural, death_rate, c='red')
        plt.title('Correlation between death rate and speed limits in rural')
        plt.xlabel('Speed limit (km/h)')
        plt.ylabel('Average death rate (deaths per 100,000 people)')

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    def graph2_urban(self, frame: ttk.Frame):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # scatter chart
        rural, death_rate, urban = self.graph2_setup()

        plt.scatter(urban, death_rate, c='blue')
        plt.title('Correlation between death rate and speed limits in urban')
        plt.xlabel('Speed limit (km/h)')
        plt.ylabel('Average death rate (deaths per 100,000 people)')

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    def graph3(self, frame: ttk.Frame):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # pie chart
        g3_df = DF_OC.rename(columns={'age_0_4': 'Under 5', 'age_5_14': '5-14 years', 'age_15_49': '15-49 years',
                                   'age_50_69': '50-69 years', 'age_70': '70+ years'})

        age_arr = ['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years']
        g3_df = g3_df.groupby(['Entity'])[age_arr].mean().mean()
        g3_df.plot.pie(startangle=90, counterclock=False, autopct='%1.2f%%', figsize=(8, 6),
                       textprops={'color': 'black'}, pctdistance=1.15, labels=None)
        plt.title('Deaths percents for different age ranges')
        plt.legend(['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years'], bbox_to_anchor=(1, 0.5))

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    def graph4(self, frame: ttk.Frame):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # pie chart
        g4_df = DF_OC.rename(columns={'type_pedestrian': 'pedestrian', 'type_motorvehicle': 'motor vehicle',
                                   'type_motorcyclist': 'motorcyclist', 'type_cyclist': 'cyclist',
                                   'type_other': 'other'})

        type_arr = ['pedestrian', 'motor vehicle', 'motorcyclist', 'cyclist', 'other']
        g4_df = g4_df.groupby(['Entity'])[type_arr].mean().mean()
        g4_df.plot.pie(startangle=90, counterclock=False, autopct='%1.2f%%', figsize=(8, 6),
                       textprops={'color': 'black'}, pctdistance=1.15, labels=None)
        plt.title('Deaths percents for different types')
        plt.legend(['pedestrian', 'motor vehicle', 'motorcyclist', 'cyclist', 'other'], bbox_to_anchor=(1, 0.5))

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    def graph5(self, frame: ttk.Frame):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # bar graph
        g5_df = copy.deepcopy(DF_OC)
        g5_col = {'age_0_4': 'Under 5', 'age_5_14': '5-14 years', 'age_15_49': '15-49 years',
                  'age_50_69': '50-69 years', 'age_70': '70+ years'}
        for col in g5_col:
            g5_df[g5_col[col]] = g5_df[col] / g5_df['population'] * 1e5

        age_arr = ['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years']
        g5_df = g5_df.groupby(['Entity'])[age_arr].mean().sum()
        g5_df.plot.bar(figsize=(8, 6), rot=0)
        plt.title('Average annual global death rate for each age range')
        plt.xlabel('Age')
        plt.ylabel('Death rate (deaths per 100,000 people)')

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    def graph6(self, frame: ttk.Frame):
        # figure
        fig = plt.figure(figsize=(8, 6))

        # bar graph
        g6_df = copy.deepcopy(DF_OC)
        g6_col = {'type_pedestrian': 'pedestrian', 'type_motorvehicle': 'motor vehicle',
                  'type_motorcyclist': 'motorcyclist', 'type_cyclist': 'cyclist', 'type_other': 'other'}
        for col in g6_col:
            g6_df[g6_col[col]] = g6_df[col] / g6_df['population'] * 1e5

        type_arr = ['pedestrian', 'motor vehicle', 'motorcyclist', 'cyclist', 'other']
        g6_df = g6_df.groupby(['Entity'])[type_arr].mean().sum()
        g6_df.plot.bar(figsize=(8, 6), rot=0)
        plt.title('Average annual global death rate for each type')
        plt.xlabel('Type')
        plt.ylabel('Death rate (deaths per 100,000 people)')

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        return canvas.get_tk_widget()

    def stat(self, frame: ttk.Frame):
        stat_df = DF_OC[['Year', 'death_total', 'death_rate']]
        stat_df = stat_df.rename(columns={'Year': '', 'death_total': 'Total deaths', 'death_rate': 'Death rate'})
        listBox = ttk.Treeview(frame)

        desc = stat_df.describe()

        listBox["column"] = list(desc.columns)
        listBox["show"] = "headings"

        for column in listBox["column"]:
            listBox.heading(column, text=column)
            listBox.column(column, anchor=tk.CENTER)

        desc = stat_df.describe().reset_index().to_numpy().tolist()

        for row in desc:
            listBox.insert("", "end", values=row)

        return listBox


if __name__ == '__main__':
    import main
