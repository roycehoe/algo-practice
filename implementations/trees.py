"""
---
Binary tree
---
Needs drawing. Refer to my notion page. Will make public when I feel like it, maybe never.
https://www.notion.so/Binary-tree-82430e06a5a74005a807b8e76b4862f7
https://www.youtube.com/watch?v=fAAZixBzIAI


---
Graph algo
---
"""

# graph


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def depth_first_while(graph, source):
    # LIFO
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for i in graph[current]:
            stack.append(i)


def depth_first_recursive(graph, source):
    print(source)
    for i in graph[source]:
        depth_first_recursive(graph, i)


def breath_first_while(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for i in graph[current]:
            queue.append(i)


def breath_first_recursive(graph, source):
    print(source)
    for i in graph[source]:
        breath_first_recursive(graph, i)

###


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


"""
Undirected graph
    https://youtu.be/tWVWeAqZ0WU?t=2553

You can move between nodes

Note: To ensure you don't cycle through the nodes, create a 'visited' list

Step 1: Create ajacency list

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


"""
Undirected path
"""
