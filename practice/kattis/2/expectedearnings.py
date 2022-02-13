"""
https://open.kattis.com/problems/expectedearnings
"""

n, k, p = input("").split()
n = int(n)
k = int(k)
p = float(p)

# if (p*n*k) < 0:
#     print("spela")
# else:
#     print("spela inte!")

if p < float(0.500000000):
    print("spela")
else:
    print("spela inte!")
