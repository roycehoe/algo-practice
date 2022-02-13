graph = {
    'i': ['j'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

visited = set()


def has_path_directed(graph, source, destination, visited):
    queue = [source]

    while len(queue) > 0:
        current_node = queue.pop(0)
        visited.add(current_node)

        if current_node == destination:
            return True
        else:
            connected_nodes = graph.get(current_node)
            for node in connected_nodes:

                if node not in visited:
                    queue.append(node)
                    visited.add(node)

    return False


print(has_path_directed(graph, 'k', 'j', visited))
