import math
import random

import tkinter as tk

from tree.node import Node
from tree.associations import create_node_associations


def node_clicked(event, canvas, nodes):
    node_index = canvas.find_closest(event.x, event.y)[0]
    node = nodes.get(node_index)
    if node:
        node.node_state.set(1)


class NodeFrame(tk.Frame):

    num_nodes = 10

    def __init__(self, master=None, **kwargs):
        self.node_loaction_blocks = []
        super().__init__(master=master, **kwargs)
        self.node_links = create_node_associations(10)
        self.canvas = tk.Canvas()
        self.canvas.config(width=600, height=600, bg='white')
        self.canvas.pack()
        self.nodes = self.create_nodes()

        self.canvas.bind('<Button-1>', lambda event, canvas=self.canvas, nodes=self.nodes: node_clicked(event, canvas, nodes))
        # self.canvas.coords(canvas_id)

        for link in self.node_links:
            first_node_index = link[0]
            sec_node_index = link[1]

            first_node = self.nodes[first_node_index]
            second_node = self.nodes[sec_node_index]

            first_x = first_node.x
            first_y = first_node.y
            second_x = second_node.x
            second_y = second_node.y

            dist = math.sqrt((first_x-second_x)**2 + (first_y-second_y)**2) - first_node.radius - second_node.radius

            first_node.associations.update({sec_node_index: {'node': second_node, 'dist': dist}})
            second_node.associations.update({first_node_index: {'node': first_node, 'dist': dist}})

            self.canvas.create_line(first_x, first_y, second_x, second_y, fill='#ccc')

            # Will redraw the nodes on top of the lines, but this makes the associations hard to follow
            # first_node.draw_node()
            # second_node.draw_node()

        self.canvas.bind('<Configure>', self.resize_canvas)

    def create_nodes(self):
        nodes = {}
        random.seed()
        for index in range(0, self.num_nodes):
            found_coord = False
            attempts = 0
            while not found_coord:
                x = random.randint(35, 500)
                y = random.randint(35, 500)
                attempts += 1
                valid_point = True
                for old_x, old_y in self.node_loaction_blocks:
                    if (x >= (old_x - 62) and x <= (old_x + 62)) and (y >= (old_y - 62) and y <= (old_y + 62)):
                        valid_point = False

                if not self.node_loaction_blocks:
                    found_coord = True

                if valid_point:
                    found_coord = True

                if attempts > 500:
                    # Catch to prevent an infinite loop if we run out of available coordinates
                    found_coord = True

            self.node_loaction_blocks.append((x, y))

            print(x, y)

            node = Node(self.canvas, index, x, y)
            nodes.update({index: node})

        return nodes

    def resize_canvas(self, event):
        self.canvas.config(width=event.width, height=event.height)


root = tk.Tk()
gui = NodeFrame(master=root, width=600, height=600, bg='white')
root.geometry('600x500')
root.title = "Node Tree"
root.mainloop()
