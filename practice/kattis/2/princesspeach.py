"""https://open.kattis.com/problems/princesspeach"""

n, y = input("").split()
n = int(n)
y = int(y)

obstacle_set = set(i for i in range(0, n))
got_set = set()

for i in range(0, y):
    got = input("")
    got = int(got)
    got_set.add(got)

for missed in obstacle_set.difference(got_set):
    print(missed)

print(f"Mario got {len(got_set)} of the dangerous obstacles.")
