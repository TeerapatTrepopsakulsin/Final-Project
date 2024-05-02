import graph_generator
import graph_ui
from controller import *

generator = GraphGenerator()
controller = Controller(generator)
ui = graph_ui.GraphUI(controller)
ui.run()
