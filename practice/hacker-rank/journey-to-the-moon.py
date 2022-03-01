"""https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true"""

"""
A = [1,2,3]
B = [1,2,3]

Possible combinations = len(A) * len(B)
"""

"""
For first element, traverse and store count in list
Keep doing this until list is exhausted
Multiply all counts together

[4,1,1]
ans = 4 * (1+1)

[4,1,1,1]
ans = 4 * (1+1+1)

[4,2]
ans = 4 * 2

"""


from math import factorial
n = 5
astronaut = [[0, 1], [2, 3], [0, 4]]
adj_list = {}

for i in range(n):
    adj_list[i] = []

for x, y in astronaut:
    if y not in adj_list[x]:
        adj_list[x].append(y)
    if x not in adj_list[y]:
        adj_list[y].append(x)

visited = set()
stack = []
ans_list = []

for start_node in range(n):
    if start_node not in visited:
        count = 0
        stack.append(start_node)

        while len(stack) > 0:
            current_node = stack.pop()
            visited.add(current_node)
            count += 1
            connected_nodes = adj_list.get(current_node)
            for connected_node in connected_nodes:
                if connected_node not in visited:
                    visited.add(connected_node)
                    stack.append(connected_node)

        ans_list.append(count)

non_wildcard_ans = 1
for i in ans_list:
    if i != 1:
        non_wildcard_ans *= i

wildcard_ans = 0
wildcard_count = 0
for i in ans_list:
    if i == 1:
        wildcard_count += 1

wildcard_ans = 0 if wildcard_count <= 1 else factorial(wildcard_count)

wildcard_with_non_wildcard_ans = wildcard_count * non_wildcard_ans
ans = wildcard_with_non_wildcard_ans + wildcard_ans + non_wildcard_ans

print(ans_list)
print(ans)
