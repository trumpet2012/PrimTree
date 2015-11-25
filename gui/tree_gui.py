import random
import tkinter as tk

from tree.node import Node


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

        self.canvas = tk.Canvas()
        self.canvas.config(width=600, height=600)
        self.canvas.pack()
        self.nodes = self.create_nodes()

        self.canvas.bind('<Button-1>', lambda event, canvas=self.canvas, nodes=self.nodes: node_clicked(event, canvas, nodes))

        node1 = self.nodes[2]
        node2 = self.nodes[4]
        self.canvas.create_line(node1.x, node1.y, node2.x, node2.y, fill='black')

    def create_nodes(self):
        nodes = {}
        random.seed()
        for index in range(0, self.num_nodes):
            found_coord = False
            attempts = 0
            while not found_coord:
                x = random.randint(0, 500)
                y = random.randint(0, 500)
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
            [nodes.update({canvas_id: node}) for canvas_id in node.canvas_ids]

        return nodes

root = tk.Tk()
gui = NodeFrame(master=root, width=600, height=600)

root.geometry('600x500')
root.title = "Node Tree"
root_canvas = tk.Canvas()
root.mainloop()
