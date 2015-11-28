import random
import tkinter as tk


class Node(tk.Frame):
    radius = 30

    def __init__(self, parent, name, x, y):
        super().__init__(parent, cnf={})
        size = self.radius * 2
        self.canvas = parent
        self.x = x
        self.y = y
        self.name = name
        self.node_state = tk.IntVar()
        self.node_color = tk.StringVar()
        self.node_color.set('#ccc')
        self.canvas_ids = {}

        def node_state_change(node_state, node_color, *args):
            if node_state.get() == 0:
                node_color.set('#ccc')
            elif node_state.get() == 1:
                node_color.set('#f00')
            # Redraw the node with the updated color
            self.draw_node()

        self.node_state.trace_variable('w', lambda *args: node_state_change(self.node_state, self.node_color))
        self.draw_node()

    def draw_node(self):
        x = self.x
        y = self.y
        radius = self.radius
        oval_id = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=self.node_color.get(), outline='white')
        text_id = self.canvas.create_text(x, y, text=self.name)
        self.canvas_ids = {'oval': oval_id, 'label': text_id}

    def get_bounding_box(self):
        x = self.x
        y = self.y
        radius = self.radius

        return x - radius, y - radius, x + radius, y + radius

    def mark_visited(self):
        self.node_state = 1
