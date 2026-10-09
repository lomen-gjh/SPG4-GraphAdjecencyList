from tkinter import *
window = Tk()
l1=Label(window, text="Zadaj meno vrcholu")
e1=Entry(window)
l2=Label(window, text="Zadaj cenu hrany")
e2=Entry(window)
b1=Button(window, text="Vynuluj graf", command=lambda:reset_graph()) #treba dorobit command...
b2=Button(window, text="Vyfarby", command=lambda:graph_coloring())
b3=Button(window, text="Vynuluj graf", command=lambda:reset_graph())
canvas = Canvas(window,width=800, height=600, bg='white')
canvas.pack(side="right")
for i in l1,e1,l2,e2,b1,b2,b3:
    i.pack()

from Graph import Graph
g=Graph() #create a graph object
oznac=None
count=1
def create_node(event):
    global g, e1, count
    if e1.get()!="":
        g.addNode(e1.get(),event.x,event.y)
    else:
        g.addNode("A"+str(count),event.x,event.y)
        count+=1
    g.draw(canvas)

def connect_node(event):
    global oznac
    for node in g.nodes:
        if g.nodes[node].x-15<=event.x<g.nodes[node].x+15 and g.nodes[node].y-15<=event.y<g.nodes[node].y+15:
            if oznac==None:
                print("OZnac")
                oznac=node
            else:
                print("Spoj")
                if oznac!=node:
                    g.connectNodes(oznac, node, int(e2.get()))
                    g.draw(canvas)
                oznac = None
def delete_node(event):
    for node in g.nodes:
        if g.nodes[node].x - 15 <= event.x < g.nodes[node].x + 15 and g.nodes[node].y - 15 <= event.y < g.nodes[node].y + 15:
            g.deleteNode(node)
            g.draw(canvas)
            return
canvas.bind("<Button-1>", create_node) #bind funkcie create_node na mouse event Button 1
canvas.bind("<Button-2>",delete_node)
canvas.bind("<Button-3>", connect_node)

#ZADANIE 2: Prepojte vrcholy pravym klikom => 1. klik si zapamata Vrchol, 2. klik prepoji oznaceny vrchol s aktualnym, osetrite Nespravne vstupy
#Zadanie 3: Kliknutim stredneho tlacidla sa vymaze vrchol aj so vsetkymi jeho hranami


def graph_coloring():
    g.graphColoring()
    g.draw(canvas)

def reset_graph():
    g.nodes={}
    g.draw(canvas)

canvas.mainloop()