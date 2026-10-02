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


    def disconnect_neighbours(self):
        for n in self.neighbours:  #pre kazdeho suseda
            for i in range(len(n[0].neighbours)): #prejdi susedovych susedov
                if n[0].neighbours[i][0]==self: #ked najdem self medzi susedovimy susedmi
                    n[0].neighbours.remove(n[0].neighbours[i]) #tak odstran dvojicu [vrchol, cena]
                    break #ukonci vnutorny cyklus
        self.neighbours=[] #zrusime vstah zo susedmi na self vrchole


