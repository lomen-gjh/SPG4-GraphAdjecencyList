from heapq import heappush, heappop
from itertools import count
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
            #used with graph coloring algorithm
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
        #mark used colors to be reused
        used_colors = set()
        for node in self.nodes.values():
            #set of colors that cannot be used with the current node
            neighbour_colors = set()
            #itterate as a pair, as neighbours are pairs of nodes and edges
            for neighbour, edge_price in node.neighbours:
                if neighbour.color is not None:
                    neighbour_colors.add(neighbour.color)
            #available colors should be used colors that are not in neighbours
            available_colors = used_colors-neighbour_colors
            if available_colors:
                # get the next available color in available_colors
                color=next(iter(available_colors))
            else:
                #no colors available, we need to generate a new one
                color=f"#{random.randint(0,0xFFFFFF):06x}"
                #while loop checks for duplicate colors
                while color in used_colors:
                    color=f"#{random.randint(0,0xFFFFFF):06x}"
                used_colors.add(color) #add the new color to used color
            node.color = color #assign the color (either from available ones or new one) to node.color


    def dijkstra_path(self, start, end, canvas):
        #reset graph for dijkstra
        for value in self.nodes.values():
            value.price=float("inf") #cena je nekonecno
            value.prev=None
        sequence=count()
        queue = [(0,next(sequence),start)]
        start.price=0 #set the first node to 0
        #we stop when the queue is empty
        while queue:
            NodePrice, order, node = heappop(queue)
            if NodePrice!=node.price:
                continue

            if node==end:
                break
            #check neighbors
            for neighbour, edge_price in node.neighbours:

                if neighbour.price>node.price+edge_price:
                    neighbour.price=node.price+edge_price
                    neighbour.prev=node
                    heappush(queue,(neighbour.price, next(sequence), neighbour))

        self.draw(canvas)
        self.drawPath(end, canvas)
        return end.price

    def drawPath(self, node, canvas):
        while node.prev != None:
            canvas.create_line(node.x, node.y, node.prev.x, node.prev.y, fill='blue', width=2)
            node = node.prev