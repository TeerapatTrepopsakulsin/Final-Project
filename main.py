"""Main block"""
from graph_generator import GraphGenerator, DefaultGraphCatalog
from graph_ui import GraphUI
from controller import Controller

generator = GraphGenerator()
catalog = DefaultGraphCatalog
controller = Controller(generator, catalog)
ui = GraphUI(controller)
ui.run()
