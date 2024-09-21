class EdgeList:
    def __init__(self):
        self.edges = []

    def add_edge(self, src, dest):
        self.edges.append((src, dest))

    def remove_edge(self, src, dest):
        self.edges = [(s, d) for s, d in self.edges if not (s == src and d == dest)]

    def edge_exists(self, src, dest):
        return (src, dest) in self.edges

    def __str__(self):
        return str(self.edges)

#Example Usage
def main():
    # Using Edge List
    edge_list = EdgeList()
    edge_list.add_edge('A', 'B')
    edge_list.add_edge('B', 'C')
    print("Edge List:", edge_list)

if __name__ == "__main__":
    main()