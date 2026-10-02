from tkinter import *
canvas = Canvas(width=800, height=600, bg='white')
canvas.pack()
from Graph import Graph
g=Graph() #create a graph object

#Test drawing
g.addNode("A", 100, 100)
g.addNode("B", 200, 100)
g.addNode("C", 150, 200)
g.connectNodes("A", "B", 5)
g.connectNodes("A", "C", 10)
g.connectNodes("B", "C", 5)
g.draw(canvas)
g.deleteNode("C")
g.draw(canvas)


canvas.mainloop()