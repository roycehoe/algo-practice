"""
"""

profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50


"""
table[capacity_index][item_index]
"""

item_count = len(profits)
table = [[0 for i in range(capacity + 1)] for i in range(item_count+1)]

for item_index in range(item_count+1):
    for capacity_index in range(capacity+1):

        if capacity_index == 0 or item_index == 0:
            table[item_index][capacity_index] = 0

        elif capacity_index > weights[item_index-1]:
            item_profit = profits[item_index-1]
            item_weight = weights[item_index - 1]

            profit_with_item = item_profit + \
                table[item_index][capacity_index-item_weight]

            profit_without_item = table[item_index-1][capacity_index]

            table[capacity_index][item_index] = max(
                profit_with_item, profit_without_item)
        else:
            table[capacity_index][item_index] = table[capacity_index][item_index-1]

print(table)
