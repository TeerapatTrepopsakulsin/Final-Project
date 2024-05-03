"""Main block"""
from graph_generator import GraphGenerator
from graph_ui import GraphUI
from controller import Controller

generator = GraphGenerator()
controller = Controller(generator)
ui = GraphUI(controller)
ui.run()
