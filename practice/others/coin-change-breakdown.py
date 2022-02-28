"""https://www.geeksforgeeks.org/coin-change-dp-7/"""

amount = 4
coin_values = [8, 1, 3, 2]
coin_count = len(coin_values)

ans_table = [0 for i in range(amount+1)]
ans_table[0] = 1

for coin_index in range(coin_count):
    coin_value = coin_values[coin_index]
    for ans_index in range(coin_value, amount+1):
        ans_table[ans_index] += ans_table[ans_index - coin_value]

print(ans_table[amount])
