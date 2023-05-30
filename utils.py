# Python3 program to find the shortest
# path between any two nodes using
# Floyd Warshall Algorithm.
 
# Initializing the distance and
# Next array
class FloydWarshel:
    def __init__(self):
        self.INF = 10**7
        MAXM = 200
        self.dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
        self.Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]
    
    def initialise(self):
        for i in range(self.V):
            for j in range(self.V):
                self.dis[i][j] = self.graph[i][j]
    
                # No edge between node
                # i and j
                if (self.graph[i][j] == self.INF):
                    self.Next[i][j] = -1
                else:
                    self.Next[i][j] = j
 
    # Function construct the shortest
    # path between u and v
    def constructPath(self, u, v):  
        # If there's no path between
        # node u and v, simply return
        # an empty array
        if (self.Next[u][v] == -1):
            return {}
    
        # Storing the path in a vector
        path = [u]
        while (u != v):
            u = self.Next[u][v]
            path.append(u)
    
        return path
 
    # Standard Floyd Warshall Algorithm
    def floydWarshall(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    
                    # We cannot travel through
                    # edge that doesn't exist
                    if (self.dis[i][k] == self.INF or self.dis[k][j] == self.INF):
                        continue
                    if (self.dis[i][j] > self.dis[i][k] + self.dis[k][j]):
                        self.dis[i][j] = self.dis[i][k] + self.dis[k][j]
                        self.Next[i][j] = self.Next[i][k]
 
    # Print the shortest path
    def printPath(self, path):
        n = len(path)
        for i in range(n - 1):
            print(path[i], end=" -> ")
        print (path[n - 1])


    def get_res(self, V, graph, a, b):
        # Function to initialise the
        # distance and Next array
        self.V = V
        self.graph = graph
        self.initialise()
    
        # Calling Floyd Warshall Algorithm,
        # this will update the shortest
        # distance as well as Next array
        self.floydWarshall()
        path = []
    
        # Path from node 1 to 3
        print(f"Shortest path from {a} to {b}: ", end = "")
        path = self.constructPath(a, b)
        self.printPath(path)