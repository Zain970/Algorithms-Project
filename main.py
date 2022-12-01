class Graph:

    def __init__(self):
        
        self.G = {

        }

    def insertEdge(self,vertex1,vertex2):


        # UNDIRECTED GRAPH
        # Appending new edge
        if self.G.get(vertex1) is None:
            self.G[vertex1] = []
            self.G[vertex1].append(vertex2)
        
        else:
            if vertex2 not in self.G[vertex1]:
                self.G[vertex1].append(vertex2)

                

        # Appending new edge
        if self.G.get(vertex2) is None:
            self.G[vertex2] = []
            self.G[vertex2].append(vertex1)
        
        else:
            if vertex1 not in self.G[vertex2]:
                self.G[vertex2].append(vertex1)

    def Bfs(self,start):

        # OPENING FILE FOR WRITING THE RESULT OF BFS
        f = open("bfs.txt", "w");

        visited = []
        queue = []

        # APPENDING STARTING NODE
        queue.append(start)

        # IF QUEUE IS NOT EMPTY
        while len(queue)!= 0:

            vertex = queue.pop(0)
            f.write(vertex + " ")
            # print(vertex,end=" ")

            # VISITED AND NO NEED
            visited.append(vertex)

            neighbours=[]

            
            if self.G.get(vertex) is not None: 
                for element in self.G[vertex]:
                    neighbours.append(element)
                
            neighbours.sort()

            for neighbour in neighbours:
                if neighbour not in queue and neighbour not in visited:
                    # WAITING IN THE QUEUE
                    queue.append(neighbour)
                

            
        print("*************** END OF BFS HELLO *****************")

    @staticmethod
    def buildGraphFromFileData():

        # Graph
        G1 = Graph();
        # OPENING FILE FOR READING
        f = open("facebook.txt", "r");

        lineNumber = 0;
        while True:

            # READING FILE LINE BY LINE
            line = f.readline();

            if len(line) == 0:
                print("Yes no more lines left ")
                break

            # Removing extra line character from the line
            line = line.replace("\n","")
            line = line.split(" ");
            
            vertex1 = line[0];
            vertex2 = line[1];

            G1.insertEdge(vertex1,vertex2);
            lineNumber+=1;
            
        print("Line number : ",lineNumber)
        f.close();
        return G1;

    def Digistra(self):
        print("Digitra");

    def 



G1 = Graph.buildGraphFromFileData();

# print(G1.G)

print("Total nodes : ",len(G1.G.keys()))

G1.Bfs("0");  // 15
G1.Dfs("");   // 15
G1.Digistra("");  // 20
G1.degree();   // 20

# G1.Digistra();
# G1

print(G1.G);
            
        
        


