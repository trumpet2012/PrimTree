import tkinter as tk


class NodeFrame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)

        self.canvas = tk.Canvas()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.canvas.create_oval(60, 60, 0, 0, fill="red")
        self.canvas.create_oval(60, 60, 120, 120, fill="blue")
        self.canvas.create_text(20, 10, text="Node Tree")
        self.canvas.pack()

gui = NodeFrame()

gui.master.title = "Node Tree"
gui.mainloop()
