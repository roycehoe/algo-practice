"""
Given an undirected graph, source, and destination node, return a boolean value depending on whether you can travel from the source node to the destination node. Do this using breath first and depth first searches.

https://youtu.be/tWVWeAqZ0WU?t=2553

---Challenge---
Undirected graphs means that using a traditional search, you might be caught in an infinite loop. This is because, you could travel from A to B and back to A indefinitely.

---Implementation---

 - To solve this, you will need to create a 'visited' set that stores the nodes that you have visited. 
 - Before you travel to any node, check if it is in the 'visited' set 
 - If it is, skip it. Else, travel to it
 - After that, append the node you traveled to to the set


Note: In Python, use a set instead of a list to check if value exists as it improves runtime performance.
"""

graph = {
    'i': ['j'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

visited = {}  # using a set since set is faster to check if value is in object


def has_path_depth(graph, source, destination, visited):
    if source == destination:
        return True
    if source in visited:
        return False

    visited.add(source)

    for i in graph[source]:
        if has_path_depth(graph, i, destination, visited):
            return True
    return False
