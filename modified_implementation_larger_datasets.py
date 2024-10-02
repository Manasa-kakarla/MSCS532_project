from collections import defaultdict, deque
import heapq
import itertools

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(set)  # Use a set for efficient neighbor operations
        self.weights = {}  # Store weights for edges

    def add_node(self, node):
        self.adjacency_list[node]  # Implicitly creates a set if the node doesn't exist

    def add_edge(self, u, v, weight=1):
        self.adjacency_list[u].add(v)
        self.adjacency_list[v].add(u)
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight  # For undirected graph

    def batch_add_edges(self, edges):
        for u, v, weight in edges:
            self.add_edge(u, v, weight)

    def remove_edge(self, u, v):
        if v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)
            del self.weights[(u, v)]
            del self.weights[(v, u)]

    def remove_node(self, node):
        if node in self.adjacency_list:
            for neighbor in list(self.adjacency_list[node]):
                self.remove_edge(node, neighbor)
            del self.adjacency_list[node]
            # Remove any weights related to this node
            for (u, v) in list(self.weights.keys()):
                if u == node or v == node:
                    del self.weights[(u, v)]

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, set())

    def get_weight(self, u, v):
        return self.weights.get((u, v), float('inf'))

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)
    print()

def dfs(graph, start):
    visited = set()
    stack = [start]  # Use a stack for iterative DFS

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)
    print()

def dijkstra(graph, start):
    min_heap = [(0, start)]
    distances = {node: float('inf') for node in graph.adjacency_list}
    distances[start] = 0
    visited = set()
    
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph.get_neighbors(current_node):
            weight = graph.get_weight(current_node, neighbor)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Example Usage
if __name__ == "__main__":
    graph = Graph()
    # Adding nodes and edges
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.batch_add_edges([('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1)])

    print("BFS Traversal:")
    bfs(graph, 'A')

    print("DFS Traversal:")
    dfs(graph, 'A')

    print("Dijkstra's Algorithm from A:")
    distances = dijkstra(graph, 'A')
    print(distances)
