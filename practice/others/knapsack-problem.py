"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
https://www.youtube.com/watch?v=nLmhmB6NzcM&t=706s

value
weight
W -> Knapsack capacity
"""


def create_dp_table(knapsack_capacity, item_count):
    return [[0 for i in range(knapsack_capacity + 1)] for i in range(item_count + 1)]


def get_profit_without_new_item(dp_table, item, capacity):
    """
    Gets profit in the previous row
    """
    return dp_table[item - 1][capacity]


def get_profit_with_new_item(dp_table, items, item, capacity, weights):
    """

    """
    return items[item-1] + dp_table[item-1][capacity-weights[item-1]]


def item_can_fit_knapsack(weights, item, capacity):
    """
    Checks if weight of {item} is less than the capacity of the knapsack
    """
    return weights[item-1] <= capacity


def get_max_profit(knapsack_capacity, weights, items):
    item_count = len(items)
    dp_table = create_dp_table(knapsack_capacity, item_count)

    # Build dp_table in bottom up manner
    for item in range(item_count + 1):
        for capacity in range(knapsack_capacity + 1):

            # profit is zero if capacity or item index is zero (ie. no items)
            if item == 0 or capacity == 0:
                dp_table[item][capacity] = 0

            if item_can_fit_knapsack(weights, item, capacity):
                profit_without_new_item = get_profit_without_new_item(
                    dp_table, item, capacity)
                profit_with_new_item = get_profit_with_new_item(
                    dp_table, items, item, capacity, weights)

                dp_table[item][capacity] = max(
                    profit_with_new_item, profit_without_new_item)
            else:
                dp_table[item][capacity] = get_profit_without_new_item(
                    dp_table, item, capacity)

    return dp_table[item_count][knapsack_capacity]


profits = [60, 100, 120]
weights = [10, 20, 30]
knapsack_capacity = 50
print(get_max_profit(knapsack_capacity, weights, profits))
# print(create_dp_table(knapsack_capacity, len(items)))
