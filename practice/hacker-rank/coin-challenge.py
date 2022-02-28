"""https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=true"""

n = 3
c = [8, 3, 1, 2]

c_count = len(c)
ans_table = [0 for i in range(n+1)]
ans_table[0] = 1

for coin_index in range(c_count):
    current_coin_value = c[coin_index]

    for ans_index in range(current_coin_value, n+1):
        ans_table[ans_index] += ans_table[ans_index - current_coin_value]

print(ans_table[n])
