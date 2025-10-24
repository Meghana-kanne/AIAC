class Graph:
    def __init__(self):
        # Initializes an empty adjacency list to represent the graph
        self.adj_list = {}

    def add_edge(self, src, dest):
        # Adds an edge from src to dest (undirected graph)
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def bfs(self, start):
        # Performs Breadth-First Search (BFS) starting from the given node
        visited = set()           # Tracks visited nodes to avoid repetition
        queue = []                # Queue for BFS
        traversal = []            # List to store the order of BFS traversal

        queue.append(start)
        visited.add(start)

        while queue:
            # Take the first node from the queue
            node = queue.pop(0)
            traversal.append(node)    # Record the node in BFS order

            # Explore all adjacent nodes (neighbors)
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)  # Enqueue the unvisited neighbor
                    visited.add(neighbor)   # Mark as visited

        return traversal

    def dfs(self, start):
        # Performs Depth-First Search (DFS) starting from the given node
        visited = set()           # Tracks visited nodes
        traversal = []            # List to store the order of DFS traversal

        def dfs_recursive(node):
            visited.add(node)         # Mark this node as visited
            traversal.append(node)    # Record the node in DFS order

            # Visit all the neighbors recursively
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return traversal

# Example Usage:
if __name__ == '__main__':
    # Creating a graph instance
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    # Performing BFS and DFS traversals
    print("BFS Traversal:", g.bfs('A'))   # Output: BFS Traversal: ['A', 'B', 'C', 'D', 'E']
    print("DFS Traversal:", g.dfs('A'))   # Output: DFS Traversal: ['A', 'B', 'D', 'C', 'E']
