from Node import Node
class Graph:
    def __init__(self):
        self.nodes={}

    def addNode(self, data, x, y):
        if data not in self.nodes: #checks for a key value
            self.nodes[data]=Node(data, x, y) #data is also a key value
        else:
            print(f"{data} already exists")

    def connectNodes(self, data1, data2, edgePrice):
        if data1 in self.nodes and data2 in self.nodes:
            self.nodes[data1].connect(self.nodes[data2], edgePrice)

    def draw(self, canvas):
        if len(self.nodes)>0:
            self.nodes[0].draw([], canvas)