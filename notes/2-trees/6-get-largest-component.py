"""
Largest component

Given an undirected graph, find the value of the largest component



"""

graph = {
    '0': ['8', '1', '5'],
    '1': ['0'],
    '5': ['0', '8'],
    '8': ['0', '5'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['3', '2']
}


def get_component_size(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1

    for i in graph[node]:
        size += get_component_size(graph, i, visited)

    return size


def get_largest_component_count(graph):
    visited = {}
    longest = 0

    for i in graph:
        size = get_component_size(graph, i, visited)
        if size > longest:
            longest = size

    return longest
