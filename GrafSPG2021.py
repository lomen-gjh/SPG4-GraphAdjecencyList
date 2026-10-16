from heapq import heappop, heappush
from itertools import count
class Node:
    NodeID=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.neighbors=[]
        self.id=Node.NodeID
        self.price=float('inf') # initial value for Dijkstra. Updated with Dijkstra alg.
        self.prev=None #used for reference to previous node, so that final shortest path can be drawn
        Node.NodeID+=1

    def add(self, node, price):
        self.neighbors.append([node, price])
        node.neighbors.append([self, price])


    def remove(self, node):
       for i in self.neighbors:
            if i[0] == node:
                self.neighbors.remove(i)
                node.neighbors.remove([self, i[1]])
                break
    #nod needed for Dijkstra
    def __lt__(self, other):
        return self.price<other.price

class Graph:
    def __init__(self):
        self.nodes=[]

    def insert(self, x,y):
        self.nodes.append(Node(x,y))

    def connect(self, nodea, nodeb,price):
        nodea.add(nodeb, price)

    def remove(self, node):
        print(node.neighbors)
        while node.neighbors!=[]:
            node.remove(node.neighbors[0][0])
            print(node.neighbors)
        self.nodes.remove(node)


    def Dijkstra(self, start, end, canvas):
        # Reset all nodes so this run does not reuse values from an earlier run.
        for i in self.nodes:
            i.price = float('inf')  # Initially, every node is treated as unreachable.
            i.prev = None  # No predecessor is known for any shortest path yet.

        # The heap is ordered by distance. The counter breaks ties, so Python
        # never needs to compare two Node objects when distances are equal.
        sequence = count()
        queue = [(0, next(sequence), start)]  # Seed the search with the start node.
        start.price = 0  # Reaching the start from itself costs zero.

        while queue:
            # Take the queued route with the lowest tentative distance.
            distance, _, node = heappop(queue)

            # A node may be queued more than once. Skip this entry if a better
            # route was found after the entry was added.
            if distance != node.price:
                continue

            # The destination is finalized once removed with its best distance.
            if node is end:
                break

            # Examine each outgoing edge, stored as [neighbor node, edge weight].
            for neighbor, weight in node.neighbors:
                # Find the total cost of reaching this neighbor through node.
                new_distance = distance + weight

                # Keep this route only if it improves the best known distance.
                if new_distance < neighbor.price:
                    neighbor.price = new_distance
                    neighbor.prev = node  # Used later to reconstruct the route.
                    # Queue the improved route so the neighbor can be explored.
                    heappush(queue, (new_distance, next(sequence), neighbor))

        # Redraw the graph, then draw the predecessor chain ending at end.
        self.draw(canvas)
        self.drawPath(end, canvas)
        return end.price  # This remains infinity if end cannot be reached.


    def prim(self, start, canvas):
        for i in self.nodes:
            i.price=1000000 #resetni cenu
            i.prev=None #resteni predchodcu
        l = []
        start.price = 0
        heappush(l,start)
        visited=[]
        print(self.nodes[0].price)
        while l:  #Primov alg.: pokial mam nieco v heape
            aktualna=heappop(l)
            if aktualna in visited:
                continue
            for pair in aktualna.neighbors: #pre vsetkych susedov l[0]
                print("Node "+str(aktualna.id)+" Sused "+str(pair[0].id))
                if pair[0].price>pair[1] and pair[0] not in visited: #ak je cena suseda vacsia ako cena hrany
                    pair[0].price = pair[1] #tak nastav cenu suseda na cenu hrany
                    pair[0].prev=aktualna #nastav susedov.prev na l[0]
                    heappush(l,pair[0])
            visited.append(aktualna) #vyhod l[0]
            print()
            for i in visited:
                print(i.id, end=' ')
            print()
            if aktualna!=start:
                print("Aktualna predchodca:"+str(aktualna.prev.id))
                #nakreslit:
        self.drawMST(canvas)
        print(self.nodes[4].prev.id)



    def draw(self, canvas):
        canvas.delete("all")
        for i in self.nodes:
            canvas.create_oval(i.x-20, i.y-20, i.x+20, i.y+20)
            canvas.create_text(i.x, i.y,text=i.id, font="Arial 11 bold")
            for j in i.neighbors:
                canvas.create_line(i.x, i.y, j[0].x, j[0].y, fill='grey')
                canvas.create_text((i.x+j[0].x)/2,(i.y+j[0].y)/2, text=j[1], font="Arial 13 bold")


    def drawPath(self, end, canvas):
        node=end
        while node.prev!=None:
            canvas.create_line(node.x, node.y, node.prev.x, node.prev.y, fill='blue', width=2)
            node=node.prev

    def drawMST(self,canvas):
        self.draw(canvas)

        for node in self.nodes:
            if node.prev!=None:
                print(str(node.id)+":"+str(node.prev.id))
                canvas.create_line(node.x, node.y, node.prev.x, node.prev.y, fill="green", width=3)
            else:
                print(str(node.id)+":None")




