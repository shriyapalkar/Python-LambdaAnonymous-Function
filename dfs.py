from collections import defaultdict #dfs algo
class Graph: # This class represents a directed graph using # adjacency list representation
	def __init__(self): # Constructor 
		self.graph = defaultdict(list) # Default dictionary to store graph
	def addEdge(self, u, v): 	# Function to add an edge to graph
		self.graph[u].append(v)
	
	def DFSUtil(self, v, visited): # A function used by DFS
		
		visited.add(v) # Mark the current node as visited # and print it
		print(v, end=' ')
		
		for neighbour in self.graph[v]: # Recur for all the vertices # adjacent to this vertex
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)
	
	def DFS(self, v): # recursive DFSUtil() # The function to do DFS traversal. It uses
		
		visited = set() # Create a set to store visited vertices
		self.DFSUtil(v, visited) # to print DFS traversal # Call the recursive helper function
if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)
	print("Following is Depth First Traversal (starting from vertex 2)")
	g.DFS(2) # Function call
# This code is contributed by Neelam Yadav
