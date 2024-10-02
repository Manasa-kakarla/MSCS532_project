from collections import defaultdict, deque
from typing import Dict, Set, List, Optional
import weakref

class User:
    def __init__(self, name: str, age: Optional[int] = None, location: Optional[str] = None):
        self.name = name
        self.age = age
        self.location = location

    def update_attributes(self, age: Optional[int] = None, location: Optional[str] = None):
        if age is not None:
            self.age = age
        if location is not None:
            self.location = location

class UserRegistry:
    def __init__(self):
        self._users = weakref.WeakValueDictionary()

    def add_user(self, user: User):
        self._users[user.name] = user

    def get_user(self, name: str) -> Optional[User]:
        return self._users.get(name)

class Graph:
    def __init__(self):
        self.adj_list: Dict[str, Set[str]] = {}

    def add_user(self, user_name: str) -> None:
        if user_name not in self.adj_list:
            self.adj_list[user_name] = set()

    def clear_graph(self):
        self.adj_list.clear()  # Free memory

# Example batch processing
def process_users_in_batches(user_generator, batch_size: int):
    batch = []
    for user in user_generator:
        batch.append(user)
        if len(batch) >= batch_size:
            # Process batch
            print(f"Processing batch of {len(batch)} users")
            batch.clear()  # Clear the batch to free memory
    if batch:
        print(f"Processing remaining {len(batch)} users")

# Usage of memory profiling
if __name__ == "__main__":
    user_registry = UserRegistry()
    graph = Graph()

    # Load users from a file (simulated here with a generator)
    def user_generator():
        for i in range(10000):  # Simulating large data
            yield User(name=f"User{i}", age=i % 50, location=f"Location{i % 10}")

    process_users_in_batches(user_generator(), batch_size=1000)

