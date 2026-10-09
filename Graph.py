import random
from Node import Node
class Graph:
    def __init__(self):
        self.nodes={}

    def addNode(self, data, x, y):
        if data not in self.nodes: #checks for a key value
            self.nodes[data]=Node(data, x, y) #data is also a key value
        else:
            print(f"{data} already exists")

    #Connect two nodes, only if they are in self.nodes dictionary
    def connectNodes(self, data1, data2, edgePrice):
        if data1 in self.nodes and data2 in self.nodes:
            self.nodes[data1].connect(self.nodes[data2], edgePrice)

    def draw(self, canvas):
        canvas.delete("all")
        for node in self.nodes.values():
            #edge is a pair: [neighbour_node, edge_price]
            for edge in node.neighbours:
                canvas.create_line(node.x, node.y, edge[0].x, edge[0].y)
                ex=(node.x+edge[0].x)/2
                ey=(node.y+edge[0].y)/2
                canvas.create_text(ex, ey, text=edge[1]) #price drawn at mid point
        #Separate loop for edges, so it looks nice :)
        for node in self.nodes.values():
            if node.color:
                canvas.create_oval(node.x - 15, node.y - 15, node.x + 15, node.y + 15, fill=node.color)
            else:
                canvas.create_oval(node.x - 15, node.y - 15, node.x + 15, node.y + 15, fill="white")
            canvas.create_text(node.x, node.y, text=node.data)

    def deleteNode(self, data):
        if data in self.nodes:
            self.nodes[data].disconnect_neighbours()
            self.nodes.pop(data)

    def graphColoring(self):
        #reset colors
        for node in self.nodes.values():
            node.color = None
        used_colors = set()
        for node in self.nodes.values():
            neighbour_colors = set()
            for neighbour, edge_price in node.neighbours:
                if neighbour.color is not None:
                    neighbour_colors.add(neighbour.color)

            available_colors = used_colors-neighbour_colors
            if available_colors:
                color=next(iter(available_colors))
            else:
                color=f"#{random.randint(0,0xFFFFFF):06x}"
                while color in used_colors:
                    color=f"#{random.randint(0,0xFFFFFF):06x}"
                used_colors.add(color)
            node.color = color