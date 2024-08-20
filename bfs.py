from collections import defaultdict # from a given source vertex. BFS(int s) traverses vertices reachable from s.
class Graph: # This class represents a directed graph # using adjacency list representation
    def __init__(self):     # Constructor
        self.graph = defaultdict(list)  # Default dictionary to store graph
    def addEdge(self, u, v): # Function to add an edge to graph
        self.graph[u].append(v)
    def BFS(self, s):  # Function to print a BFS of graph
        visited = [False] * (max(self.graph) + 1) # Mark all the vertices as not visited
        queue = [] # Create a queue for BFS
        queue.append(s)  # Mark the source node as # visited and enqueue it
        visited[s] = True
        while queue:
            s = queue.pop(0) # Dequeue a vertex from# queue and print it
            print(s, end=" ")
            for i in self.graph[s]: # Get all adjacent vertices of the # dequeued vertex s.# If an adjacent has not been visited,# then mark it visited and enqueue it
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
if __name__ == '__main__': # Driver code
    g = Graph()     # Create a graph given in # the above diagram
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    g.BFS(2)


