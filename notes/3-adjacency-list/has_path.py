graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path(graph, source, destination):
    queue = [source]

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node == destination:
            return True
        else:
            connected_nodes = graph.get(current_node)
            for node in connected_nodes:
                queue.append(node)

    return False
