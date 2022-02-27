"""https://www.geeksforgeeks.org/coin-change-dp-7/"""

coin_values = [2, 5, 3, 6]
coin_count = len(coin_values)
available_change = 10

table = [[0 for current_change in range(
    available_change+1)] for coin_index in range(coin_count+1)]

for coin_index in range(coin_count+1):
    for current_change in range(available_change+1):

        if current_change == 0:
            table[coin_index][current_change] = 1
        elif coin_index == 0:
            table[coin_index][current_change] = 0
        else:
            ans = 0
            current_coin_value = coin_values[coin_index-1]

            if coin_index >= 1:
                ans += table[coin_index - 1][current_change]

            if current_change >= current_coin_value:
                ans += table[coin_index][current_change - current_coin_value]

            table[coin_index][current_change] = ans


print(table)
