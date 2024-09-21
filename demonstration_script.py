class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, src, dest):
        self.add_node(src)
        self.add_node(dest)
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)

    def remove_edge(self, src, dest):
        if src in self.adjacency_list and dest in self.adjacency_list[src]:
            self.adjacency_list[src].remove(dest)
            self.adjacency_list[dest].remove(src)

    def __str__(self):
        return str(self.adjacency_list)

class EdgeList:
    def __init__(self):
        self.edges = []

    def add_edge(self, src, dest):
        self.edges.append((src, dest))

    def __str__(self):
        return str(self.edges)

class AttributeTable:
    def __init__(self):
        self.data = {}

    def add_node_attribute(self, node, attribute):
        self.data[node] = attribute

    def get_attributes(self, node):
        return self.data.get(node, "No attributes")

    def __str__(self):
        return str(self.data)

def main():
    # Initialize data structures
    graph = Graph()
    edge_list = EdgeList()
    attribute_table = AttributeTable()

    # Adding users
    users = ['Alice', 'Bob', 'Charlie', 'David']
    for user in users:
        attribute_table.add_node_attribute(user, {'age': 20 + users.index(user), 'location': 'City' + str(users.index(user))})
        print(f"Added user: {user} with attributes: {attribute_table.get_attributes(user)}")

    # Establishing connections (friendships)
    connections = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David')]
    for src, dest in connections:
        graph.add_edge(src, dest)
        edge_list.add_edge(src, dest)
        print(f"Established connection between {src} and {dest}.")

    # Display current state of the graph
    print("\nCurrent state of the Graph (Friendships):")
    print(graph)

    # Display Edge List
    print("\nCurrent Edge List:")
    print(edge_list)

    # Display Attribute Table
    print("\nUser Attributes:")
    print(attribute_table)

    # Removing a connection
    graph.remove_edge('Alice', 'Bob')
    print("\nAfter removing the connection between Alice and Bob:")
    print(graph)

    # Displaying attributes of a specific user
    print("\nAttributes of Charlie:")
    print(attribute_table.get_attributes('Charlie'))

if __name__ == "__main__":
    main()
