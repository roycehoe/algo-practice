"""https://open.kattis.com/problems/tajna"""

# ui = input()
# n = len(ui)

# n = 16
# r = 1

# for i in range(1, n+1):
#     if n % i == 0:
#         temp_r = i
#         temp_c = int(n/r)

#         if temp_r > temp_c:
#             break

#         r = i
#         c = int(n/r)

word = "bok"
r = 1
c = 2

test = [i for i in word]

for i in range(0, c):
    print(test[i::r])
