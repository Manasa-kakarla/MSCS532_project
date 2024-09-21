class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, src, dest, directed=False):
        self.add_node(src)
        self.add_node(dest)
        self.adjacency_list[src].append(dest)
        if not directed:
            self.adjacency_list[dest].append(src)

    def remove_edge(self, src, dest):
        if self.edge_exists(src, dest):
            self.adjacency_list[src].remove(dest)
            if not self.is_directed():
                self.adjacency_list[dest].remove(src)

    def remove_node(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for neighbors in self.adjacency_list.values():
                if node in neighbors:
                    neighbors.remove(node)

    def edge_exists(self, src, dest):
        return src in self.adjacency_list and dest in self.adjacency_list[src]

    def is_directed(self):
        # Optional: implement logic to determine if graph is directed
        return False

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in self.adjacency_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        return visited

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(set(self.adjacency_list[node]) - visited)
        return visited

    def __str__(self):
        return str(self.adjacency_list)

#Example Usage
def main():
    # Using Graph
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    print("Graph Adjacency List:", graph)
    print("DFS from A:", graph.dfs('A'))
    print("BFS from A:", graph.bfs('A'))

if __name__ == "__main__":
    main()