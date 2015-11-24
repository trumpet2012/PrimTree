import random
import tkinter as tk

from itertools import cycle

from tree.node import Node


class NodeFrame(tk.Frame):

    num_nodes = 10

    def __init__(self, master=None):
        super().__init__(master=master)

        self.canvas = tk.Canvas()
        self.nodes = self.create_nodes()

    def create_nodes(self):
        nodes = []
        random.seed()
        for index in range(0, self.num_nodes):
            x = random.randint(0, 20)
            y = random.randint(0, 20)
            print(x, y)
            node = Node(self, index, x, y)
            nodes.append(node)

        return nodes

gui = NodeFrame()

gui.master.title = "Node Tree"
gui.mainloop()
