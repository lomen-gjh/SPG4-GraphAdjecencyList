from tkinter import *
window = Tk()
l1=Label(window, text="Zadaj meno vrcholu")
e1=Entry(window)
l2=Label(window, text="Zadaj cenu hrany")
e2=Entry(window)
b1=Button(window, text="Vynuluj graf", command=lambda:reset_graph()) #treba dorobit command...
canvas = Canvas(window,width=800, height=600, bg='white')
canvas.pack(side="right")
for i in l1,e1,l2,e2,b1:
    i.pack()

from Graph import Graph
g=Graph() #create a graph object

def create_node(event):
    global g, e1
    g.addNode(e1.get(), event.x, event.y)
    g.draw(canvas)

canvas.bind("<Button-1>", create_node) #bind funkcie create_node na mouse event Button 1

#ZADANIE 2: Prepojte vrcholy pravym klikom => 1. klik si zapamata Vrchol, 2. klik prepoji oznaceny vrchol s aktualnym, osetrite Nespravne vstupy
#Zadanie 3: Kliknutim stredneho tlacidla sa vymaze vrchol aj so vsetkymi jeho hranami

def reset_graph():
    print("Tato funkcia vynuluje graf")

canvas.mainloop()