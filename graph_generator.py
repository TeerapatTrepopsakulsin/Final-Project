import copy
from tkinter import ttk
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum
from abc import ABC

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DF = pd.read_csv("data.csv")
DF_OC = pd.read_csv("data_only_country.csv")


class GraphGenerator(ABC):
    def __init__(self):
        self.__start_year = 1990
        self.__end_year = 2019
        self.__entity1 = 'World'
        self.__entity2 = 'Thailand'
        self.__unit = 'death_rate'
        self.__array = ['death_rate']
        self.__mode = 'standard'
        self.__graph = 'Histogram'
        self.__og_df = DF_OC
        self.__og_df_name = "Only Country"

    def get_generator(self) -> 'GraphGenerator':
        attr = copy.copy(self.__dict__)
        if self.graph == 'Line Graph':
            return LinegraphGenerator(**attr)
        elif self.graph == 'Histogram':
            return HistogramGenerator(**attr)
        elif self.graph == 'Bar Graph':
            return BargraphGenerator(**attr)
        elif self.graph == 'Stat':
            return StatGenerator(**attr)

    def generate(self, frame: ttk.Frame, size, process="normal"):
        """
        Generate the visualisation.

        :param frame: ttk.Frame
        :param size: tuple with length of 2. For example, (4, 3)
        :param process: str: "normal" or "entity" or "top5"
        :return:
        """
        pass

    def setup(self, **kwargs):
        for item in kwargs:
            if '_GraphGenerator__' + item not in self.__dict__:
                raise ValueError(f'unknown option "-{item}"')
        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_all(self):
        self.og_df = DF
        self.og_df_name = 'All'

    def set_only_country(self):
        self.og_df = DF_OC
        self.og_df_name = 'Only country'

    def array_to_label(self):
        to_label = {'age_0_4': 'Under 5', 'age_5_14': '5-14 years', 'age_15_49': '15-49 years',
                    'age_50_69': '50-69 years', 'age_70': '70+ years', 'type_pedestrian': 'pedestrian',
                    'type_motorvehicle': 'motor vehicle', 'type_motorcyclist': 'motorcyclist',
                    'type_cyclist': 'cyclist', 'type_other': 'other', 'death_rate': 'death rate',
                    'death_total': 'total deaths'}

        label_list = list(map(lambda x: to_label[x], copy.deepcopy(self.array)))
        return label_list

    @property
    def start_year(self):
        return self.__start_year

    @start_year.setter
    def start_year(self, year):
        if not isinstance(year, int):
            raise TypeError('Year should be integer.')
        if year < 1990 or year > 2019:
            raise ValueError('Year should be between 1990 to 2019.')
        self.__start_year = year

    @property
    def end_year(self):
        return self.__end_year

    @end_year.setter
    def end_year(self, year):
        if not isinstance(year, int):
            raise TypeError('Year should be an integer.')
        if year < 1990 or year > 2019:
            raise ValueError('Year should be between 1990 to 2019.')
        self.__end_year = year

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph):
        available = ("Histogram", "Line Graph", "Bar Graph", "Stat")
        if graph not in available:
            raise ValueError('Available graph types are: "Histogram", "Line Graph", "Bar Graph", "Stat"')
        self.__graph = graph

    @property
    def entity1(self):
        return self.__entity1

    @entity1.setter
    def entity1(self, entity):
        self.__entity1 = entity

    @property
    def entity2(self):
        return self.__entity2

    @entity2.setter
    def entity2(self, entity):
        self.__entity2 = entity

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        available = ("death_rate", "death_total")
        if unit not in available:
            raise ValueError('Available units are: "death_rate", "death_total"')
        self.__unit = unit

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, arr):
        if not arr:
            raise ValueError('Array cannot be empty.')
        self.__array = arr

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        available = ("standard", "top5")
        if mode not in available:
            raise ValueError('Available modes are: "standard", "top5"')
        self.__mode = mode

    @property
    def og_df(self):
        return self.__og_df

    @og_df.setter
    def og_df(self, df):
        self.__og_df = df

    @property
    def og_df_name(self):
        return self.__og_df_name

    @og_df_name.setter
    def og_df_name(self, name):
        self.__og_df_name = name


class LinegraphGenerator(GraphGenerator):
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
        self.df_gen = DataframeGenerator(**self.__dict__)
        if self.mode == 'standard':
            self.process = 'entity'
        if self.mode == 'top5':
            self.process = 'top5'

    def generate(self, frame: ttk.Frame, size, process="entity"):
        if process != "entity" and process != "top5":
            raise ValueError('line graph generating process can only be "entity", "top5".')

        # figure
        fig, ax = plt.subplots(figsize=size)

        # line graph
        l_df = self.df_gen.generate(frame, size, self.process)
        en_arr = l_df['Entity'].unique()

        for entity in en_arr:
            entity_df = l_df[l_df['Entity'] == entity]

            yval = entity_df[self.array].sum(axis=1)

            ax.plot(entity_df['Year'], yval)

        width = (self.end_year - self.start_year) // 12 + 1
        ax.set_xticks(range(self.start_year, self.end_year + 1, width))
        ax.grid()
        ax.tick_params(axis='x', grid_linewidth=0.3)

        to_label = {
            'death_rate': ('death rate', 'Death rate (deaths per 100,000 people)'),
            'death_total': ('total deaths', 'Total deaths (people)')
        }
        ax.set_ylabel(f'{to_label[self.unit][1]}')
        ax.set_xlabel('Year')
        ax.set_title(f'Line graph of {to_label[self.unit][0]} from road incidents')
        ax.legend(en_arr, title='Entity')

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def __del__(self):
        pass


class BargraphGenerator(GraphGenerator):
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
        self.df_gen = DataframeGenerator(**self.__dict__)
        if self.mode == 'standard':
            self.process = 'entity'
        if self.mode == 'top5':
            self.process = 'top5'

    def generate(self, frame: ttk.Frame, size, process="entity"):
        if process != "entity" and process != "top5":
            raise ValueError(f'bar graph generating process can only be "entity", "top5"; not {process}')

        # figure

        fig, ax = plt.subplots(figsize=size)

        # bar graph
        b_df = self.df_gen.generate(frame, size, self.process)
        groupby_df = b_df[['Entity'] + self.array].groupby(['Entity']).mean()
        en_arr = groupby_df.index
        type_arr = self.array

        # set width of bar
        bar_width = 1 / (len(en_arr) + 1)

        # Make the plot
        colour_arr = ['royalblue', 'orange', 'forestgreen', 'firebrick', 'mediumpurple']
        for i in range(len(en_arr)):
            br = [x + i * bar_width for x in np.arange(len(type_arr))]
            en = groupby_df.iloc[i]
            clr = colour_arr[i]
            plt.bar(br, en, color=clr, width=bar_width, label=en_arr[i])

        to_label = {
            'death_rate': ('death rate', 'Death rate (deaths per 100,000 people)'),
            'death_total': ('total deaths', 'Total deaths (people)')
        }
        plt.ylabel(f'{to_label[self.unit][1]}')
        plt.title(f'Average annual {to_label[self.unit][0]} in {self.start_year} - {self.end_year}')
        plt.grid()
        plt.xticks([r + 0.5 * (len(en_arr) - 1) * bar_width for r in range(len(type_arr))], self.array_to_label())
        plt.tick_params(axis='x', grid_linewidth=0)
        plt.legend(title='Entity')

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def __del__(self):
        pass


class HistogramGenerator(GraphGenerator):
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
        self.df_gen = DataframeGenerator(**self.__dict__)

    def generate(self, frame: ttk.Frame, size, process="normal"):
        if process != "normal":
            raise ValueError('histogram generating process can only be "normal".')
        # figure
        fig = plt.figure(figsize=size)

        # histogram
        h_df = self.df_gen.generate(frame, size, process)  # histogram can generate only 1 mode anyway
        hist = h_df[self.array].sum(axis=1).hist(bins=20)
        to_label = {
            'death_rate': ('death rate', 'Death rate (deaths per 100,000 people)'),
            'death_total': ('total deaths', 'Total deaths (people)')
        }
        plt.title(f'Histogram for {to_label[self.unit][0]} from road incidents in {self.start_year}')
        plt.xlabel(f'{to_label[self.unit][1]}')
        plt.ylabel('Frequency (Countries)')
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def __del__(self):
        pass


class StatGenerator(GraphGenerator):
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
        self.df_gen = DataframeGenerator(**self.__dict__)

    def generate(self, frame: ttk.Frame, size, process='normal') -> 'ttk.Treeview':
        if process != "normal":
            raise ValueError('statistic generating process can only be "normal".')

        df = self.df_gen.generate(frame, size, process)  # stat can generate only 1 mode anyway
        stat_df = df[['death_total', 'death_rate']]
        stat_df = stat_df.rename(columns={'death_total': 'Total deaths', 'death_rate': 'Death rate'})
        des_stat = stat_df.describe()
        col = [''] + list(des_stat.columns)
        table = ttk.Treeview(frame, columns=col, show='headings')
        table.configure(style='Treeview')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 12, 'bold'))
        style.configure("Treeview", font=(None, 11))

        for column in table["column"]:
            table.heading(column, text=column)
            table.column(column, anchor=tk.CENTER, width=10)

        des_stat_list = stat_df.describe().reset_index().to_numpy().tolist()

        for row in des_stat_list:
            table.insert("", "end", values=row)

        table.configure(height=10)

        return table

    def __del__(self):
        pass


class DataframeGenerator(GraphGenerator):
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)

    def generate(self, frame: ttk.Frame, size, process="normal"):
        df = copy.deepcopy(self.og_df)
        if process == "normal":
            new_df = df[df['Year'] == self.start_year]
            gen_df = self.initialise(new_df)
            return gen_df

        new_df = df[(df['Year'] >= self.start_year) &
                    (df['Year'] <= self.end_year)]

        if process == 'entity':
            new_df = new_df[(new_df['Entity'] == self.entity1) | (new_df['Entity'] == self.entity2)]

        gen_df = self.initialise(new_df)

        if process == "top5":
            groupby_df = gen_df.groupby(['Entity'])[self.array].mean()
            top_arr = groupby_df.sum(axis=1).sort_values(ascending=False)
            top_arr = top_arr.index[:5]
            gen_df = gen_df[(gen_df['Entity'] == top_arr[0]) |
                            (gen_df['Entity'] == top_arr[1]) |
                            (gen_df['Entity'] == top_arr[2]) |
                            (gen_df['Entity'] == top_arr[3]) |
                            (gen_df['Entity'] == top_arr[4])]

        return gen_df

    def initialise(self, df):
        if self.unit == 'death_total':
            return df

        new_df = copy.deepcopy(df)
        df_col = ['age_0_4', 'age_5_14', 'age_15_49', 'age_50_69', 'age_70',
                  'type_pedestrian', 'type_motorvehicle', 'type_motorcyclist',
                  'type_cyclist', 'type_other']
        for col in df_col:
            new_df[col] = new_df[col] / new_df['population'] * 1e5

        return new_df

    def __del__(self):
        pass


class DefaultGraph:
    def __init__(self):
        pass

    def graph1(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # bar graph
        g1_df = DF_OC.groupby(['seatbelt_law'])['death_rate'].mean()

        colour = np.array(['red', 'green'])

        g1_df.plot(kind='bar', stacked=False, xlabel='Existence of seat-belt law',
                   ylabel='Average death rate (deaths per 100,000 people)', color=colour, rot=0, grid=True)
        plt.tick_params(axis='x', grid_linewidth=0)
        plt.title('Average death rate of countries with and without seat-belt law')
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    @staticmethod
    def graph2_setup():
        g2_df = DF_OC.groupby(['Entity'])[['death_rate', 'rural_speed_limit', 'urban_speed_limit']].mean()

        a = g2_df['rural_speed_limit']
        b = g2_df['death_rate']
        c = g2_df['urban_speed_limit']

        return a, b, c

    def graph2(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # scatter chart
        rural, death_rate, urban = self.graph2_setup()

        plt.scatter(rural, death_rate, c='red')
        plt.scatter(urban, death_rate, c='blue')
        plt.title('Correlation between death rate and speed limits')
        plt.xlabel('Speed limit (km/h)')
        plt.ylabel('Average death rate (deaths per 100,000 people)')
        plt.legend(['rural', 'urban'])
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def graph2_rural(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # scatter chart
        rural, death_rate, urban = self.graph2_setup()

        plt.scatter(rural, death_rate, c='red')
        plt.title('Correlation between death rate and speed limits in rural')
        plt.xlabel(f'Speed limit (km/h)\nCorrelation coefficient: {rural.corr(death_rate)}')
        plt.ylabel('Average death rate (deaths per 100,000 people)')
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def graph2_urban(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # scatter chart
        rural, death_rate, urban = self.graph2_setup()

        plt.scatter(urban, death_rate, c='blue')
        plt.title('Correlation between death rate and speed limits in urban')
        plt.xlabel(f'Speed limit (km/h)\nCorrelation coefficient: {urban.corr(death_rate)}')
        plt.ylabel('Average death rate (deaths per 100,000 people)')
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def graph3(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # pie chart
        g3_df = DF_OC.rename(columns={'age_0_4': 'Under 5', 'age_5_14': '5-14 years', 'age_15_49': '15-49 years',
                                      'age_50_69': '50-69 years', 'age_70': '70+ years'})

        age_arr = ['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years']
        g3_df = g3_df.groupby(['Entity'])[age_arr].mean().mean()
        g3_df.plot.pie(startangle=90, counterclock=False, autopct='%1.2f%%',
                       textprops={'color': 'black'}, pctdistance=1.15, labels=None)
        plt.title('Deaths percents for different age ranges')
        plt.legend(['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years'], bbox_to_anchor=(1, 0.5))
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def graph4(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # pie chart
        g4_df = DF_OC.rename(columns={'type_pedestrian': 'pedestrian', 'type_motorvehicle': 'motor vehicle',
                                      'type_motorcyclist': 'motorcyclist', 'type_cyclist': 'cyclist',
                                      'type_other': 'other'})

        type_arr = ['pedestrian', 'motor vehicle', 'motorcyclist', 'cyclist', 'other']
        g4_df = g4_df.groupby(['Entity'])[type_arr].mean().mean()
        g4_df.plot.pie(startangle=90, counterclock=False, autopct='%1.2f%%',
                       textprops={'color': 'black'}, pctdistance=1.15, labels=None)
        plt.title('Deaths percents for different types')
        plt.legend(['pedestrian', 'motor vehicle', 'motorcyclist', 'cyclist', 'other'], bbox_to_anchor=(1, 0.5))
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def graph5(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # bar graph
        g5_df = copy.deepcopy(DF_OC)
        g5_col = {'age_0_4': 'Under 5', 'age_5_14': '5-14 years', 'age_15_49': '15-49 years',
                  'age_50_69': '50-69 years', 'age_70': '70+ years'}
        for col in g5_col:
            g5_df[g5_col[col]] = g5_df[col] / g5_df['population'] * 1e5

        age_arr = ['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years']
        g5_df = g5_df.groupby(['Entity'])[age_arr].mean().sum()
        g5_df.plot.bar(rot=0, grid=True)
        plt.tick_params(axis='x', grid_linewidth=0)
        plt.title('Average annual global death rate for each age range')
        plt.xlabel('Age')
        plt.ylabel('Death rate (deaths per 100,000 people)')
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def graph6(self, frame: ttk.Frame, size):
        # figure
        fig = plt.figure(figsize=size)

        # bar graph
        g6_df = copy.deepcopy(DF_OC)
        g6_col = {'type_pedestrian': 'pedestrian', 'type_motorvehicle': 'motor vehicle',
                  'type_motorcyclist': 'motorcyclist', 'type_cyclist': 'cyclist', 'type_other': 'other'}
        for col in g6_col:
            g6_df[g6_col[col]] = g6_df[col] / g6_df['population'] * 1e5

        type_arr = ['pedestrian', 'motor vehicle', 'motorcyclist', 'cyclist', 'other']
        g6_df = g6_df.groupby(['Entity'])[type_arr].mean().sum()
        g6_df.plot.bar(rot=0, grid=True)
        plt.tick_params(axis='x', grid_linewidth=0)
        plt.title('Average annual global death rate for each type')
        plt.xlabel('Type')
        plt.ylabel('Death rate (deaths per 100,000 people)')
        plt.tight_layout()

        # Tkinter canvas that contain the figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        plt.close(fig)
        return canvas.get_tk_widget()

    def graph7(self):
        # TODO
        # Linegraph death rate/year (speed limit range as hue)
        pass

    def __del__(self):
        pass


class DefaultGraphCatalog(Enum):

    SPD_DRAT = {'label': 'Speed limits/Death rate', 'func': DefaultGraph().graph2}
    SPD_RR_DRAT = {'label': 'Speed limits (Rural)/Death rate', 'func': DefaultGraph().graph2_rural}
    SPD_UB_DRAT = {'label': 'Speed limits (Urban)/Death rate', 'func': DefaultGraph().graph2_urban}
    SBL_DRAT = {'label': 'Seat-belt law/Death rate', 'func': DefaultGraph().graph1}
    AGE_PIE = {'label': 'Ages (Pie chart)', 'func': DefaultGraph().graph3}
    TYPE_PIE = {'label': 'Types (Pie chart)', 'func': DefaultGraph().graph4}
    AGE_BAR = {'label': 'Ages (Bar graph)', 'func': DefaultGraph().graph5}
    TYPE_BAR = {'label': 'Types (Bar graph)', 'func': DefaultGraph().graph6}

    @property
    def detail(self):
        return self.value

    def __str__(self):
        return self.name

    @staticmethod
    def get_func(label):
        for item in DefaultGraphCatalog:
            if item.value['label'] == label:
                return item.value['func']


class DatasetTreeview:
    def __init__(self):
        self.df = copy.deepcopy(DF).rename(columns={'age_0_4': 'Under 5', 'age_5_14': '5-14 years', 'age_15_49': '15-49 years',
                    'age_50_69': '50-69 years', 'age_70': '70+ years', 'type_pedestrian': 'pedestrian',
                    'type_motorvehicle': 'motor vehicle', 'type_motorcyclist': 'motorcyclist',
                    'type_cyclist': 'cyclist', 'type_other': 'other', 'death_rate': 'death rate',
                    'death_total': 'total deaths', 'urban_speed_limit': 'Urban speed limits', 'rural_speed_limit': 'Rural speed limits', 'seatbelt_law': 'Seat-belt law'})
    def get_treeview(self, frame: ttk.Frame):
        column = list(self.df)
        tree = ttk.Treeview(frame, selectmode="extended")
        tree["show"] = "headings"

        tree["columns"] = column
        for col in column:
            tree.column(col, anchor="w")
            tree.heading(col, text=col)

        for i in range(len(self.df)):
            row = self.df.iloc[i].tolist()
            tree.insert('', tk.END, values=row)

        return tree


if __name__ == '__main__':
    import main
