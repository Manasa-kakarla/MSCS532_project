Project: Developing and Optimizing Data Structures for Real-World Applications Using Python

This Project will help to understand the practical challenges of implementing and optimizing data structures in real-world scenarios, focusing on both performance

and scalability. this project will include coding the data structures, running performance tests, analyzing results, and optimizing the structures for efficiency.

'graph_representation.py': contains the code for adding, removing and searching for nodes and edges.

'adjacency_matrix.py': contains the code for functionalities like insertion, deletion, searching and traversal.

'Edge_list.py': contains the logic for key functionalities which are insertion, Deletion, Searching.

'incidence_matrix.py': contains the code for insertion, deletion and seraching of edges.

'attribute_table.py': contains the logic to implement insertion, deletion and searching of attributes.

'cli_script.py': simple command-line interface(CLI) script that demonstrates the functionality of above data structures.

'demonstration_script.py': This script will simulate a social network with users as nodes and their conncetions as edges. This will showcases basic functionalities

relevant to a social network analysis application.

prerequisites:

python3.x

Run the code:

To run above files below are the commands:

python graph_representation.py

python adjacency_matrix.py

python Edge_list.py

python incidence_matrix.py

python attribute_table.py

python cli_script.py

python demonstration_script.py

sample output of graph_representation.py:

python -u "/home/manasa/vscode_projects/MSCS532_project/graph_representation.py"

Graph Adjacency List: {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}

DFS from A: {'A', 'C', 'B'}

BFS from A: {'A', 'C', 'B'}

sample output of adjacency_matrix.py:

python -u "/home/manasa/vscode_projects/MSCS532_project/adjacency_matrix.py"

Adjacency Matrix: [[0, 1, 1], [0, 0, 0], [0, 0, 0]]

sample output of Edge_list.py:

python -u "/home/manasa/vscode_projects/MSCS532_project/Edge_list.py"

Edge List: [('A', 'B'), ('B', 'C')]

sample output of incidence_matrix.py:

python -u "/home/manasa/vscode_projects/MSCS532_project/incidence_matrix.py"

Incidence Matrix: [[1, 0], [1, 1], [0, 1]]

sample output of attribute_table.py:

python -u "/home/manasa/vscode_projects/MSCS532_project/attribute_table.py"

Attribute Table:   Node                      Attribute

0    A  {'age': 25, 'location': 'NY'}

sample output of demonstration_script.py:

python -u "/home/manasa/vscode_projects/MSCS532_project/demonstration_script.py"

Added user: Alice with attributes: {'age': 20, 'location': 'City0'}

Added user: Bob with attributes: {'age': 21, 'location': 'City1'}

Added user: Charlie with attributes: {'age': 22, 'location': 'City2'}

Added user: David with attributes: {'age': 23, 'location': 'City3'}

Established connection between Alice and Bob.

Established connection between Alice and Charlie.

Established connection between Bob and David.

Current state of the Graph (Friendships):

{'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice', 'David'], 'Charlie': ['Alice'], 'David': ['Bob']}

Current Edge List:

[('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David')]

User Attributes:

{'Alice': {'age': 20, 'location': 'City0'}, 'Bob': {'age': 21, 'location': 'City1'}, 'Charlie': {'age': 22, 'location': 'City2'}, 'David': {'age': 23, 'location': 'City3'}}

After removing the connection between Alice and Bob:

{'Alice': ['Charlie'], 'Bob': ['David'], 'Charlie': ['Alice'], 'David': ['Bob']}

Attributes of Charlie:

{'age': 22, 'location': 'City2'}

