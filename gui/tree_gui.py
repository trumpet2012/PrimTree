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
        self.canvas.config(width=600, height=600)
        self.canvas.pack()
        self.nodes = self.create_nodes()

        self.canvas.bind('<Button-1>', lambda event, canvas=self.canvas, nodes=self.nodes: node_clicked(event, canvas, nodes))
        # self.canvas.coords(canvas_id)

        for link in self.node_links:
            first_node_index = link[0]
            sec_node_index = link[1]

            first_node = self.nodes[first_node_index]
            second_node = self.nodes[sec_node_index]

            self.canvas.create_line(first_node.x, first_node.y, second_node.x, second_node.y, fill='black')

            # Will redraw the nodes on top of the lines, but this makes the associations hard to follow
            # first_node.draw_node()
            # second_node.draw_node()

        # dist = math.sqrt((circle1.x-circle2.x)**2 + (circle1.y-circle2.y)**2) - circle1.r - circle2.r

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
            nodes.update({index: node})

        return nodes

root = tk.Tk()
gui = NodeFrame(master=root, width=600, height=600)

root.geometry('600x500')
root.title = "Node Tree"
root_canvas = tk.Canvas()
root.mainloop()
