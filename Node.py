class Node:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.neighbours=[]

    def connect(self, otherNode, edgePrice):
        if otherNode==None:
            print("Cant connect with None")
            return
        index=self.find(otherNode)
        if index==None:
            self.neighbours.append([otherNode, edgePrice])
            otherNode.neighbours.append([self, edgePrice])
        else:
            #Edit edge
            self.neighbours[index][1]=edgePrice  #nastav si novu cenu
            otherIndex=otherNode.find(self) #najdi tuto hranu u suseda
            otherNode.neighbours[otherIndex][1]=edgePrice #uprav cenu aj na hrane suseda


    #CHECK not mandatory, as Node A could have more paths to Node B
    #Option: no redundancy
    def find(self, otherNode):
        for i in range(len(self.neighbours)):
            if otherNode==self.neighbours[i][0]:
                return i
        return None
    #recursive draw, so I dont have to draw the edges twice
    def draw(self, visited, canvas):
        visited.append(self.data)
        canvas.create_oval(self.x-15, self.y-15, self.x+15, self.y+15)
        canvas.create_text(self.x, self.y, text=self.data)
        for edge in self.neighbours:
            if edge[0].data not in visited:
                canvas.create_line(edge[0].x, edge[0].y, self.x, self.y)
                ex=(edge[0].x+self.x)/2
                ey=(edge[0].y+self.y)/2
                canvas.create_text(ex, ey, text=edge[1])
                edge[0].draw(visited, canvas)
