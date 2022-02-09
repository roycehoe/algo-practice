"""
Limitations of breath-first search: Does not work if you are trying to optimize travel time, not reducing total node count.
The smallest amount of nodes taken to get somewhere may not optimize travel time if the time between those nodes are large.
Flying from New York to Los Angeles has two options. New York - Atlanta - Los Angeles vs New York - Los Angeles.
But if the direct flight takes you across the entire globe and the Pacific Ocean, it might be better to take the NY-A-LA path.

Dikstra's algorithm:
 0. All nodes not directly connected to the start node is infinity
 1. Find the cheapest node
 2. Check if there is a cheaper path to the neighbours of this node. If so, update their cost
 3. Repeat for every node in the graph
 4. Calculate the final path

Note: The cost of traveling from one node to another is called weight. Dikstra's algorithm is used on weighted graphs.

"""
