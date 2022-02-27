"""https://www.geeksforgeeks.org/coin-change-dp-7/"""


def get_coin_change_count(coin_values, coin_count, available_change):
    table = [[0 for coin_index in range(coin_count)]
             for change_index in range(available_change+1)]

    # solution is 1 when change_index is zero, regardless of coin index
    for coin_index in range(coin_count):
        table[0][coin_index] = 1

    for current_change in range(1, available_change+1):
        for coin_index in range(coin_count):
            ans = 0
            current_coin_value = coin_values[coin_index]

            # Take the answer from the row above, same column [ie. takes previous ans]
            if current_change >= current_coin_value:
                ans += table[current_change - current_coin_value][coin_index]

            # Take the answer from the row above, same column [ie. takes previous ans]
            if coin_index >= 1:
                ans += table[current_change][coin_index-1]

            table[current_change][coin_index] = ans

    return table
    # return table[available_change][coin_count-1]


# Driver program to test above function
coin_values = [2, 5, 3, 6]
coin_count = len(coin_values)
available_change = 10


ans = get_coin_change_count(coin_values, coin_count, available_change)
print(ans)
