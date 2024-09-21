class AdjacencyMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, src, dest):
        self.matrix[src][dest] = 1

    def remove_edge(self, src, dest):
        self.matrix[src][dest] = 0

    def edge_exists(self, src, dest):
        return self.matrix[src][dest] == 1

    def get_neighbors(self, node):
        return [i for i in range(self.size) if self.matrix[node][i] == 1]

    def __str__(self):
        return str(self.matrix)

#Example Usage
def main():
    # Using Adjacency Matrix
    adj_matrix = AdjacencyMatrix(size=3)
    adj_matrix.add_edge(0, 1)
    adj_matrix.add_edge(0, 2)
    print("Adjacency Matrix:", adj_matrix)

if __name__ == "__main__":
    main()