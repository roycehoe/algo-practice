adj_list = {}
mylist = []  # list of all nodes


def add_node(node):
    """
    check if node is in list. If so, add. Else print error
    """
    if node not in mylist:
        mylist.append(node)
    else:
        print("Node ", node, " already exists!")


def add_edge(node1, node2):
    """
    check if both nodes is in list. Error checking

    Look at node 1. 
        If node 1 is not in the adjacency list, 
            create a dictionary entry for it. Node 1 is now a key
            For the value, set it to temp. In this case, it would be an empty list
        Else, (ie. node 1 is in the adjacency list)
            extend temp with the dictionary value of Node 1. In this case, that would be nothing. Temp would still be an empty list
            Then, append node 2 to temp. Temp now contains 1 item: node 2
            Finally, assign Temp to the key of node 1. Node 1 in the adjacency list now as node 2 as a value
    """
    temp = []

    if node1 in mylist and node2 in mylist:
        if node1 not in adj_list:
            temp.append(node2)
            adj_list[node1] = temp

        elif node1 in adj_list:
            temp.extend(adj_list[node1])
            temp.append(node2)
            adj_list[node1] = temp

    else:
        print("Nodes don't exist!")


def graph():
    for node in adj_list:
        print(node, " ---> ", [i for i in adj_list[node]])


# Adding nodes
add_node(0)
add_node(1)
add_node(2)
add_node(3)
add_node(4)
# Adding edges
add_edge(0, 1)
add_edge(1, 2)
add_edge(2, 3)
add_edge(3, 0)
add_edge(3, 4)
add_edge(4, 0)

# Printing the graph
graph()

# Printing the adjacency list
print(adj_list)
