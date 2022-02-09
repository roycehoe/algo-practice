"""https://open.kattis.com/problems/veci"""

from functools import reduce
from itertools import permutations


n = input("")
n_i = int(n)
print([int(i) for i in n])
n = list(permutations([int(i) for i in n]))


perms = []


for i in n:
    perms.append(reduce(lambda sub, ele: sub * 10 + ele, i))
perms.sort()

ans = perms[perms.index(int(n_i))+1]
if ans == n_i:
    print(0)
else:
    print(ans)
