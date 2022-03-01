profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
item_count = len(profits)

table = [0 for i in range(capacity+1)]

for item_index in range(1, item_count+1):
    for current_capacity in range(capacity, 0, -1):

        item_weight = weights[item_index-1]
        item_profit = profits[item_index - 1]

        if item_weight <= current_capacity:
            profit_without_item = table[current_capacity]
            profit_with_item = table[current_capacity -
                                     item_weight] + item_profit

            table[current_capacity] = max(
                profit_with_item, profit_without_item)

print(table)
