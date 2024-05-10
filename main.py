"""Main block"""
from graph_generator import GraphGenerator, DefaultGraphCatalog, DatasetTreeview
from graph_ui import GraphUI
from controller import Controller


generator = GraphGenerator()
catalog = DefaultGraphCatalog
dataset_treeview = DatasetTreeview()
controller = Controller(generator, catalog, dataset_treeview)
ui = GraphUI(controller)
ui.run()
