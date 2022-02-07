"""
Graph
 - Graph models are a set of connections. Think of it as degrees of separation between people. You know someone who knows someone who knows Obama.
 - You are a node. The person you know is a node. The link between you and the person you know is an edge.

Breath first search
 - Problem: How do you find the smallest degree of separation between you and Obama?
 - Two questions: Is there a path between you and Obama? What is the shortest path then?

Finding the shortest path
 - You are X. You ask your friends, A, B, C. None of them are Obama.
 - You check AA, AB, AC (A's friends). BA, BB, BC. CA, CB, CC. None of them are Obama
 - You check AAA, AAB, AAC (AA's friends); ABA, ABB, ABC ...... till you find Obama
 - Note: To do this, you need to implement a queue. 

Queue
 - Like a real life queue. You cannot access a random element. 
 - Operations:
  - Enque: Add something to the queue. Goes to the back of the line
  - Deque: Take something from the queue. Done at the start of the line. How operations are performed.

Queue vs Stack
 - Queue: FIFO - First in, first out
 - Stack: LIFO = Last in, first out

Graph implementation: Hash table
 - Example:
  - Map X to A, B, C
  - Map A to AA, AB, AC .....

Graph implementation: Steps
 - Keep a queue of A, B, C
 - Pop a person from the queue. Say A
 - Check if A is Obama
 - If yes, we found Obama
 - If no, add AA, AB, AC to the queue (all of A's friends)
 - Loop
 - If queue is empty, Obama is not within any degree of separation from you

Things to note for implementation:
 - You need some sort of condition to check if someone is Obama

 - AA may know BB. BB may know CC. CC may know AA. You might be caught in an infinite loop. Therefore, you should not add duplicates to your queue.
 - This can be done by keeping a "searched" group. When you have determined AA is not Obama, add AA to the searched group
 - Before adding anyone to the queue, check if they are a part of the searched group. If they are, do not add them to the queue. Add them otherwise.

Big O:
 - Let V = number of vertices, E for number of edges
 - You will need to check each edge. Runtime is O(E)
 - Adding people to the queue takes O(1). There are V number of people. O(V)
 - Big O is therefore O(V + E)

Topological sort:
 - Graphs that ensures that nodes that depends on other nodes show up later. Think of a family tree.
"""
