import pandas as pd

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
        return False

    def __str__(self):
        return str(self.adjacency_list)

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

    def __str__(self):
        return str(self.matrix)

class EdgeList:
    def __init__(self):
        self.edges = []

    def add_edge(self, src, dest):
        self.edges.append((src, dest))

    def remove_edge(self, src, dest):
        self.edges = [(s, d) for s, d in self.edges if not (s == src and d == dest)]

    def __str__(self):
        return str(self.edges)

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

    def __str__(self):
        return str(self.matrix)

class AttributeTable:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Node', 'Attribute'])

    def add_node_attribute(self, node, attribute):
        self.data = self.data.append({'Node': node, 'Attribute': attribute}, ignore_index=True)

    def remove_node_attribute(self, node):
        self.data = self.data[self.data['Node'] != node]

    def __str__(self):
        return str(self.data)

def display_menu():
    print("\nSelect an option:")
    print("1. Add node to Graph")
    print("2. Add edge to Graph")
    print("3. Remove edge from Graph")
    print("4. Remove node from Graph")
    print("5. Display Graph")
    print("6. Add edge to Adjacency Matrix")
    print("7. Display Adjacency Matrix")
    print("8. Add edge to Edge List")
    print("9. Display Edge List")
    print("10. Add edge to Incidence Matrix")
    print("11. Display Incidence Matrix")
    print("12. Add node attribute to Attribute Table")
    print("13. Display Attribute Table")
    print("0. Exit")

def main():
    graph = Graph()
    adj_matrix = AdjacencyMatrix(size=3)
    edge_list = EdgeList()
    inc_matrix = IncidenceMatrix(num_nodes=3, num_edges=3)
    attribute_table = AttributeTable()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            node = input("Enter node name: ")
            graph.add_node(node)
            print(f"Node '{node}' added to Graph.")
        elif choice == '2':
            src = input("Enter source node: ")
            dest = input("Enter destination node: ")
            graph.add_edge(src, dest)
            print(f"Edge from '{src}' to '{dest}' added.")
        elif choice == '3':
            src = input("Enter source node: ")
            dest = input("Enter destination node: ")
            graph.remove_edge(src, dest)
            print(f"Edge from '{src}' to '{dest}' removed.")
        elif choice == '4':
            node = input("Enter node name to remove: ")
            graph.remove_node(node)
            print(f"Node '{node}' removed from Graph.")
        elif choice == '5':
            print("Current Graph:", graph)
        elif choice == '6':
            src = int(input("Enter source index: "))
            dest = int(input("Enter destination index: "))
            adj_matrix.add_edge(src, dest)
            print(f"Edge from {src} to {dest} added to Adjacency Matrix.")
        elif choice == '7':
            print("Adjacency Matrix:", adj_matrix)
        elif choice == '8':
            src = input("Enter source node: ")
            dest = input("Enter destination node: ")
            edge_list.add_edge(src, dest)
            print(f"Edge from '{src}' to '{dest}' added to Edge List.")
        elif choice == '9':
            print("Edge List:", edge_list)
        elif choice == '10':
            src = int(input("Enter source index: "))
            dest = int(input("Enter destination index: "))
            inc_matrix.add_edge(src, dest)
            print(f"Edge from {src} to {dest} added to Incidence Matrix.")
        elif choice == '11':
            print("Incidence Matrix:", inc_matrix)
        elif choice == '12':
            node = input("Enter node name: ")
            attribute = input("Enter attribute as JSON string: ")
            attribute_table.add_node_attribute(node, attribute)
            print(f"Attribute added for node '{node}'.")
        elif choice == '13':
            print("Attribute Table:", attribute_table)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
