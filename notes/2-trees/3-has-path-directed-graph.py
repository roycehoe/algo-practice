"""
Given a directed graph, source, and destination node, return a boolean value depending on whether you can travel from the source node to the destination node. Do this using breath first and depth first searches.

---Challenge---
You now need to return a boolean value depending on whether you managed to hit the destination node

---Implementation---
 - Do a search
 - For each path you touch on, check if it is equal to the destination node. If it is, return True
 - Else, keep searching
 - If you have traversed the entire graph, return False

"""

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path_depth(graph, source, destination):
    if source == destination:
        return True

    for i in graph[source]:
        if has_path_depth(graph, i, destination):
            return True
    return False


def has_path_breath(graph, source, destination):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop()
        if current == destination:
            return True
        for i in graph[current]:
            queue.append(i)
    return False
