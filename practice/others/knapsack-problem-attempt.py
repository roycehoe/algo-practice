"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
https://www.youtube.com/watch?v=nLmhmB6NzcM&t=706s
"""


def get_max_profit(table, weight, item_index, weight_index):
    profit_without_item = table[item_index-1][weight_index]

    item_profit = profits[item_index-1]
    profit_with_item = item_profit + \
        table[item_index-1][weight_index - weight[item_index-1]]

    return max(profit_with_item, profit_without_item)


def get_max_knapsack_profit(capacity, weight, profits):
    item_count = len(profits)
    table = [[0 for i in range(capacity+1)] for i in range(item_count+1)]

    for item_index in range(item_count+1):
        for weight_index in range(capacity + 1):
            if item_index == 0 or weight_index == 0:
                table[item_index][weight_index] = 0

            elif weight[item_index-1] <= weight_index:
                table[item_index][weight_index] = get_max_profit(
                    table, weight, item_index, weight_index)
            else:
                table[item_index][weight_index] = table[item_index-1][weight_index]

    return table[item_count][capacity]

####################################################


profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(get_max_knapsack_profit(capacity, weights, profits))
# print(create_dp_table(knapsack_capacity, len(items)))
