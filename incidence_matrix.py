class IncidenceMatrix:
    def __init__(self, num_nodes, num_edges):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.matrix = [[0] * num_edges for _ in range(num_nodes)]
        self.edge_count = 0

    def add_edge(self, src, dest):
        if self.edge_count < self.num_edges:
            self.matrix[src][self.edge_count] = 1
            self.matrix[dest][self.edge_count] = 1
            self.edge_count += 1

    def remove_edge(self, edge_index):
        for i in range(self.num_nodes):
            self.matrix[i][edge_index] = 0

    def edge_exists(self, src, dest):
        for edge_index in range(self.num_edges):
            if self.matrix[src][edge_index] == 1 and self.matrix[dest][edge_index] == 1:
                return True
        return False

    def __str__(self):
        return str(self.matrix)

#Example Usage
def main():
    # Using Incidence Matrix
    inc_matrix = IncidenceMatrix(num_nodes=3, num_edges=2)
    inc_matrix.add_edge(0, 1)
    inc_matrix.add_edge(1, 2)
    print("Incidence Matrix:", inc_matrix)

if __name__ == "__main__":
    main()
