import pickle


import tkinter

from GrafSPG2021 import Graph
form=tkinter.Tk()
form.title("Graph as list of neighbors")
e1=tkinter.Entry(form)
l0=tkinter.Label(form, text="Edge weight")
l1=tkinter.Label(form,text="Start node index")
e2=tkinter.Entry(form)
l2=tkinter.Label(form, text="End node index")
e3=tkinter.Entry(form)
l0.pack()
e1.pack()
l1.pack()
e2.pack()
l2.pack()
e3.pack()
b1=tkinter.Button(form, text="Start Dijkstra", command=lambda:runDijkstra(int(e2.get()),int(e3.get())))
b1.pack()
b2=tkinter.Button(form, text="Prim", command=lambda:runPrim(int(e2.get())))
b2.pack()


b3 = tkinter.Button(form, text="dump", command=lambda: dump())
b4 = tkinter.Button(form, text="load", command=lambda: load())
b3.pack()
b4.pack()



canvas=tkinter.Canvas(form, width=600,height=400,bg='white')
canvas.pack()
graph=Graph()
marked=None



def dump():
    with open("graph.pkl", "wb") as f:
        pickle.dump(graph, f)
        f.close()

def load():
    global graph
    with open("graph.pkl", "rb") as f:
        graph = pickle.load(f)
        f.close()
    graph.draw(canvas)

def insert_Node(event):
    graph.insert(event.x,event.y)
    graph.draw(canvas)


def connect_node(event):
    global marked
    try:
        for node in graph.nodes:
            if event.x-20<node.x<=event.x+20 and event.y-20<node.y<=event.y+20:
                if marked==None:
                    marked=node
                else:
                    if marked==node:
                        pass
                    else:
                        graph.connect(node,marked, int(e1.get()))
                        marked=None
                        graph.draw(canvas)
    except ValueError as err:
        print("Zla hodnota")
    # vo for loope zistite ci ste klikli na node
    # ak ste klikli na node, tak zistite ci marked je None. Ak ano, aktualny oznacte
    # ak marked !=none a marked!= aktualny node, tak spravim ciaru a marked zase nastavim na none
        #ak marked==aktualny node, tak iba nastavte marked=None a print("Cant connect node with itself")

def remove(event):
    for node in graph.nodes:
        if event.x-20<node.x<=event.x+20 and event.y-20<node.y<=event.y+20:
            graph.remove(node)
            graph.draw(canvas)
            break

def runDijkstra(start,end):
    graph.Dijkstra(graph.nodes[start], graph.nodes[end], canvas)

def runPrim(index):
    graph.prim(graph.nodes[index], canvas)



canvas.bind("<Button-1>", insert_Node)
canvas.bind("<Button-2>", remove)
canvas.bind("<Button-3>", connect_node)
canvas.mainloop()
