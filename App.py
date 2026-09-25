from tkinter import *
canvas = Canvas(width=800, height=600, bg='white')
canvas.pack()
from Graph import Graph
g=Graph()

g.addNode("A", 100, 100)
g.addNode("B", 200, 100)
g.addNode("C", 150, 200)
g.connectNodes("A", "B", 5)
g.connectNodes("A", "C", 10)
g.draw(canvas)

canvas.mainloop()