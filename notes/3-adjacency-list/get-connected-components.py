graph = {0: [8, 1, 5],
         1: [0],
         5: [0, 8],
         8: [0, 5],
         2: [3, 4],
         3: [2, 4],
         4: [3, 2]}


visited = set()


def get_connected_components(graph, source, visited):
    queue = [source]

    while len(queue) > 0:
        current_node = queue.pop(0)
        visited.add(current_node)

        connected_nodes = graph.get(current_node)

        for node in connected_nodes:
            if node not in visited:
                visited.add(node)
                queue.append(node)

    return visited


def get_connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            visited = get_connected_components(
                graph, node, visited)
            count += 1

    return count


print(get_connected_components_count(graph))
