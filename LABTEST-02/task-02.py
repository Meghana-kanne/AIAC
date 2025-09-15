import heapq

def dijkstra(graph, source):
    # Step 1: Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    pq = [(0, source)]  # (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Step 2: Edge relaxation for all neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Algorithm Outline:
# 1. Set all node distances to infinity except the source (0).
# 2. Use a priority queue to always expand the closest node.
# 3. For each neighbor, relax the edge: if a shorter path is found, update distance and push to queue.
# 4. Repeat until all nodes are processed.

# Example usage:
if __name__ == "__main__":
    user_input = input("Enter adjacency dict (e.g. {'A':{'B':1,'C':4},'B':{'C':2,'D':5},'C':{'D':1},'D':{}}): ")
    graph = eval(user_input)
    source = 'A'
    distances = dijkstra(graph, source)
    print("Shortest distances from source:", distances)