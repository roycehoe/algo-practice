"""https://www.geeksforgeeks.org/coin-change-dp-7/"""

coin_values = [99, 2, 5, 3, 6]
coin_count = len(coin_values)
available_change = 10

######Efficient solution###########

table = [0 for change_index in range(available_change+1)]
table[0] = 1

for coin_index in range(0, coin_count):
    current_coin_value = coin_values[coin_index]

    for change_index in range(current_coin_value, available_change+1):
        table[change_index] += table[change_index - current_coin_value]
    print(f'''
Current coin value: {current_coin_value}
Start index: {current_coin_value}
End index: {available_change+1}
Table: {table}
    ''')
