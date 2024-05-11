"""Controller module"""
from tkinter import ttk
from graph_generator import GraphGenerator, DefaultGraphCatalog, DatasetTreeview
from entity import Entity


class Controller:
    """Controller connects UI to the generators."""
    def __init__(self, graph_generator: GraphGenerator,
                 default_graph: type[DefaultGraphCatalog],
                 data_tree: DatasetTreeview):
        self.catalog = default_graph
        self.generator = graph_generator
        self.data_tree = data_tree

    def initialise_stt(self, frame: ttk.Frame):
        """
        Initialise Storytelling page components.

        :param frame: ttk.Frame, Storytelling page
        :returns:
            - hist - ttk.Canvas of initial histogram
            - graph - ttk.Canvas of initial graph
            - des_stat - ttk.Treeview of initial descriptive statistics
            - default_graph_list - list of default graphs name
        """
        # initialise the generator
        self.generator.setup(start_year=2019, end_year=2019, unit='death_rate',
                             array=['death_rate'], mode='standard')
        self.generator.set_only_country()

        # generating
        size = (8, 4)
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
        """
        Return the histogram and descriptive statistics according to the specific year.

        :param frame: ttk.Frame, Storytelling page
        :param year: int
        :returns:
            - hist - ttk.Canvas of histogram
            - des_stat - ttk.Treeview of descriptive statistics
        """
        # initialise the generator
        self.generator.setup(start_year=year, end_year=year, unit='death_rate',
                             array=['death_rate'], mode='standard')
        self.generator.set_only_country()

        # generating
        size = (8, 4)

        self.generator.setup(graph='Histogram')
        generator = self.generator.get_generator()
        hist = generator.generate(frame, size)

        self.generator.setup(graph='Stat')
        generator = self.generator.get_generator()
        des_stat = generator.generate(frame, size)

        return hist, des_stat

    def handle_select_graph(self, frame: ttk.Frame, graph):
        """
        Return the graph according to the graph name.

        :param frame: ttk.Frame, Storytelling page
        :param graph: str of graph name
        :return: _graph - ttk.Canvas of graph
        """
        func = self.catalog.get_func(graph)
        size = (5, 3)
        _graph = func(frame, size)

        return _graph

    def initialise_dte(self, frame: ttk.Frame):
        """
        Initialise Data Exploration page components.

        :param frame: ttk.Frame, Data Exploration page
        :return: line - ttk.Canvas of initial line graph
        """
        # initialise the generator
        self.generator.setup(start_year=1990, end_year=2019, entity1='World', entity2='Thailand',
                             unit='death_rate', array=['death_rate'], mode='standard')
        self.generator.set_all()

        size = (8, 5)
        self.generator.graph = 'Line Graph'
        generator = self.generator.get_generator()
        line = generator.generate(frame, size)

        return line

    @staticmethod
    def get_entity_list():
        """
        Return the list of all entities.

        :return: list of all entities
        """
        en_list = Entity['ALL'].value
        return en_list

    def handle_generate(self, frame: ttk.Frame):
        """
        Return the generated graph after generate from Data Exploration page.

        :param frame: ttk.Frame, Data Exploration page
        :return: graph - ttk.Canvas of the graph
        """
        size = (8, 5)
        generator = self.generator.get_generator()
        graph = generator.generate(frame, size)

        return graph

    def get_dataset_treeview(self, frame: ttk.Frame):
        """
        Return the dataset for Dataset page.

        :param frame: ttk.Frame, Dataset page
        :return: tree - ttk.Treeview of the dataset
        """
        tree = self.data_tree.get_treeview(frame)
        return tree
