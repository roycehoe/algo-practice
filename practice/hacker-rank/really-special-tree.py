g_from = [1, 1, 4, 2, 3, 3]
g_to = [2, 3, 1, 4, 2, 4]
g_weight = [5, 3, 6, 7, 4, 5]

adj_tree = {}

nodes = set(g_from + g_to)

for node in nodes:
    adj_tree[node] = []

for path in range(len(g_from)):
    start_node = g_from[path]
    end_node = g_to[path]
    weight = g_weight[path]

    adj_tree[start_node].append([end_node, weight])

print(adj_tree)
