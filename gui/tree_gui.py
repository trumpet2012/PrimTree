import random
import tkinter as tk

from itertools import cycle

from tree.node import Node


def node_clicked(event, node):
    node.node_state.set(1)
    node.master.create_line(node.canvas.winfo_x(), node.canvas.winfo_y(), node.canvas.winfo_x()+100, node.canvas.winfo_y(), fill='black')
    node.canvas.create_rectangle(node.canvas.winfo_x()-100,node.canvas.winfo_y()-100,node.canvas.winfo_x(),node.canvas.winfo_y(), fill='black')



class NodeFrame(tk.Frame):

    num_nodes = 10

    def __init__(self, master=None):
        super().__init__(master=master)

        self.canvas = tk.Canvas()

        self.nodes = self.create_nodes()

        # self.canvas.create_line(0, 0, 500, 500, fill='black')

    def create_nodes(self):
        nodes = []
        random.seed()
        for index in range(0, self.num_nodes):
            x = random.randint(0, 20)
            y = random.randint(0, 20)
            print(x, y)

            node = Node(self.canvas, index, x, y)
            node.canvas.bind('<Button-1>', lambda event, node=node: node_clicked(event, node))
            node.canvas.grid(row=y, column=x, padx=10, pady=10)

            nodes.append(node)

        return nodes


gui = NodeFrame()

gui.master.title = "Node Tree"
gui.mainloop()
