import math
import time
import random
import heapq

import tkinter as tk

from tree.node import Node
from tree.associations import create_node_associations


def node_clicked(event, canvas, nodes):
    node_index = canvas.find_closest(event.x, event.y)[0]
    node = nodes.get(node_index)
    if node:
        node.node_state.set(1)


class NodeFrame(tk.Frame):

    num_nodes = 20

    def __init__(self, master=None, **kwargs):
        self.node_loaction_blocks = []
        super().__init__(master=master, **kwargs)
        self.node_links = create_node_associations(self.num_nodes)
        self.canvas = tk.Canvas(**kwargs)
        self.canvas.config(bg='white')
        self.canvas.pack()
        self.nodes = self.create_nodes()

        self.canvas.bind('<Button-1>', self.plot_path)
        self.link_nodes()

        self.canvas.bind('<Configure>', self.resize_canvas)

    def create_nodes(self):
        nodes = {}
        random.seed()
        for index in range(0, self.num_nodes):
            found_coord = False
            attempts = 0
            while not found_coord:
                x = random.randint(35, int(self.canvas.config('width')[4]) - 35)
                y = random.randint(35, int(self.canvas.config('height')[4]) - 35)
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

            node = Node(self.canvas, index, x, y)
            nodes.update({index: node})

        return nodes

    def resize_canvas(self, event):
        self.canvas.config(width=event.width, height=event.height)

    def link_nodes(self):
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

            line = self.canvas.create_line(first_x, first_y, second_x, second_y, fill='#ccc')

            first_node.associations.update({sec_node_index: {'node': second_node, 'dist': dist, 'line': line}})
            second_node.associations.update({first_node_index: {'node': first_node, 'dist': dist, 'line': line}})

            # Will redraw the nodes on top of the lines, but this makes the associations hard to follow
            # first_node.draw_node()
            # second_node.draw_node()

    def plot_path(self, event):
        nodes_remaining = self.nodes.copy()
        selected_nodes = []
        curr_node = nodes_remaining.pop(0)
        selected_nodes.append(curr_node)
        curr_node.mark_visited()
        while not len(nodes_remaining) == 0:
            best_path = None
            best_dist = None
            node_to_best_node = None

            for best_node in selected_nodes:
                path_options = best_node.associations
                for key, node_values in path_options.items():
                    poss_node = node_values.get('node')
                    if poss_node.node_state.get() == 1:
                        continue

                    if best_path is None:
                        best_path = key
                        node_to_best_node = best_node
                        best_dist = node_values.get('dist')
                        continue

                    if node_values.get('dist') < best_dist:
                        best_path = key
                        node_to_best_node = best_node

            curr_line = node_to_best_node.associations.get(best_path).get('line')
            self.canvas.itemconfig(curr_line, fill='red')
            next_node = nodes_remaining.pop(best_path)
            selected_nodes.append(next_node)
            next_node.mark_visited()


root = tk.Tk()
gui = NodeFrame(master=root, width=800, height=800, bg='white')
root.geometry('800x800')
root.title = "Node Tree"
root.mainloop()
