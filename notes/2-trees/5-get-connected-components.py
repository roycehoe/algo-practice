"""
Given an undirected graph, return the number of connected components. Do this using breath first and depth first searches.

---Challenge---
You now need to return an integer that represents the number of connected components

---Implementation---
Create a global 'visited' set
Create a loop that goes through each node in your graph, appending each visited node to the 'visited' set
Create an if statement that would skip a traversal if the source node has been visited before
Create a counter that increments after you complete a traversal
"""

graph = {0: [8, 1, 5],
         1: [0],
         5: [0, 8],
         8: [0, 5],
         2: [3, 4],
         3: [2, 4],
         4: [3, 2]}


def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for i in graph[current]:
        explore(graph, i, visited)

    return True


def get_connected_component_count(graph):
    visited = {}
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count
