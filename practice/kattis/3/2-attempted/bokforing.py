"""https://open.kattis.com/problems/bokforing"""

"""
n = people
Q = event

Event: Set, reset, print
Custom event: start
"""


def user_in():
    n, q = input("").split()
    n = int(n)
    q = int(q)
    pop = {}
    wealth = 0
    to_print = []

    for i in range(0, q):
        event, data = input("").split(" ", 1)

        if event == "SET":
            i, x = data.split()
            i = int(i)
            x = int(x)

            pop[i] = x
        if event == "RESTART":
            data = int(data)
            wealth = int(data)
            pop = {}
        if event == "PRINT":
            data = int(data)
            try:
                to_print.append((pop[data]))
            except Exception:
                to_print.append(wealth)

    for i in to_print:
        print(i)


user_in()
