import random
import string
import time
from threading import Thread
from collections import defaultdict

# Assuming Graph and InteractionGraph classes are defined as follows:

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(set)

    def add_user(self, user_name: str):
        self.adj_list[user_name]  # Add an entry in the adjacency list

    def add_connection(self, user1: str, user2: str):
        self.adj_list[user1].add(user2)
        self.adj_list[user2].add(user1)

    def remove_connection(self, user1: str, user2: str):
        self.adj_list[user1].discard(user2)
        self.adj_list[user2].discard(user1)

class InteractionGraph:
    def __init__(self):
        self.interactions = defaultdict(lambda: defaultdict(int))

    def add_interaction(self, user1: str, user2: str, weight: int):
        self.interactions[user1][user2] += weight

    def get_interaction_weight(self, user1: str, user2: str) -> int:
        return self.interactions[user1][user2]

# Stress test functions

def stress_test_massive_user_addition(graph, num_users=100000):
    print("Starting massive user addition stress test...")
    start_time = time.time()
    for i in range(num_users):
        graph.add_user(f"User{i}")
    end_time = time.time()
    print(f"Massive user addition completed in {end_time - start_time:.2f} seconds.")

def stress_test_high_volume_connections(graph, num_users=10000):
    print("Starting high volume of connections stress test...")
    start_time = time.time()
    for i in range(num_users):
        graph.add_connection(f"User{i}", f"User{(i + 1) % num_users}")  # Circular connections
    end_time = time.time()
    print(f"High volume of connections completed in {end_time - start_time:.2f} seconds.")

def stress_test_concurrent_operations(graph, num_users=10000):
    print("Starting concurrent operations stress test...")
    
    def add_users():
        for i in range(num_users // 2):
            graph.add_user(f"ConcurrentUser{i}")
    
    def add_connections():
        for i in range(num_users // 2):
            graph.add_connection(f"ConcurrentUser{i}", f"ConcurrentUser{(i + 1) % (num_users // 2)}")
    
    thread1 = Thread(target=add_users)
    thread2 = Thread(target=add_connections)

    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()

    print(f"Concurrent operations completed in {end_time - start_time:.2f} seconds.")

def stress_test_randomized_edge_cases(graph, num_cases=10000):
    print("Starting randomized edge cases stress test...")
    for _ in range(num_cases):
        user_name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))
        if random.choice([True, False]):
            graph.add_user(user_name)
        else:
            if random.choice([True, False]):
                graph.add_connection(user_name, "NonExistentUser")
            else:
                graph.remove_connection(user_name, "NonExistentUser")

def stress_test_interaction_graph(interaction_graph, num_users=10000):
    print("Starting interaction graph stress test...")
    for i in range(num_users):
        interaction_graph.add_interaction(f"User{i}", f"User{(i + 1) % num_users}", weight=random.randint(1, 10))
    print("Interaction graph stress test completed.")

# Run stress tests
if __name__ == "__main__":
    # Create instances of Graph and InteractionGraph
    graph = Graph()
    interaction_graph = InteractionGraph()

    # Run the stress tests
    stress_test_massive_user_addition(graph, num_users=100000)
    stress_test_high_volume_connections(graph, num_users=10000)
    stress_test_concurrent_operations(graph, num_users=10000)
    stress_test_randomized_edge_cases(graph, num_cases=10000)
    stress_test_interaction_graph(interaction_graph, num_users=10000)
