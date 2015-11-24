import tkinter as tk


class Node(tk.Frame):
    radius = 30

    def __init__(self, parent, label, x, y):
        super().__init__(parent, cnf={})
        size = self.radius*2
        self.canvas = tk.Canvas(width=size, height=size)
        self.x = x
        self.y = y
        radius = self.radius

        self.canvas.create_oval(5, 5, 60, 60, fill="green")
        self.canvas.create_text(30, 30, text=label)
        self.canvas.grid(row=y, column=x, padx=10, pady=10)

    def contains(self, x, y):
        radius = self.radius
        return x >= self.x - radius and x <= self.x + radius and y >= self.y - radius and y <= self.y + radius

    def get_bounding_box(self):
        x = self.x
        y = self.y
        radius = self.radius

        return x - radius, y - radius, x + radius, y + radius
