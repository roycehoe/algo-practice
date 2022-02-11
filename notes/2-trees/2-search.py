"""
Given a graph, traverse the entire graph with a depth first and breath first search, printing out each visited path

---Concepts---

Depth first
 - Depth first uses a stack which follows LIFO (Last in, first out)
 - A stack is represented as a list in Python
 - To add to the stack, you need to list.append(item). This puts the item at the end of the list.
 - To remove things from the stack, you need to list.pop(). This takes the last item out of the list. This follows the LIFO principle

Breath first
 - Breath first uses a stack which follows FIFO (First in, first out)
 - A queue is represented as a list in Python
 - To add to the queue, you need to list.append(item). This puts the item at the end of the list.
 - To remove things from the queue, you need to list.pop(0). This takes the first item out of the list as it pops the element at index 0. This follows the FIFO principle

---Implementation---

Depth first
 - Pop the node at the end of the list and print it
 - If there are no connecting nodes to this node, break loop
 - Else, append all connecting nodes to this node to the end of the list

 - Do the above steps till the list is empty

Breath first
 - Pop the node at the start of the list and print it
 - If there are no connecting nodes to this node, break loop
 - Else, append all connecting nodes to this node to the end of the list

 - Do the above steps till the list is empty
"""

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
