"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
https://www.youtube.com/watch?v=nLmhmB6NzcM&t=706s


Note of possible confusion:

Whenver you are dealing with the dp_table, you can use raw index
However, if you are cross referencing dp_table index with other arrays, you must deduct one
"""


def create_dp_table(knapsack_capacity, item_count):
    """
    Creates a dp table with one additional column and row to account for when
    knapsack capacity and item count is zero
    """
    return [[0 for i in range(knapsack_capacity + 1)] for i in range(item_count + 1)]


def get_profit_without_new_item(dp_table, item_index, capacity):
    """
    Gets profit stored in previous row, same column
    """
    return dp_table[item_index - 1][capacity]


def get_profit_with_new_item(dp_table, profits, item_index, capacity, weights):
    # get item profit from profit table
    # index is -1 because {item} comes from built table which has additional row and column
    item_profit = profits[item_index-1]

    # index is -1 because {item} comes from built table which has additional row and column
    item_weight = weights[item_index - 1]
    new_capacity = capacity - item_weight
    profit_with_modified_capacity = dp_table[item_index - 1][new_capacity]

    return item_profit + profit_with_modified_capacity


def item_can_fit_knapsack(weights, item_index, capacity):
    """
    Checks if weight of {item} is less than the capacity of the knapsack
    """
    return weights[item_index-1] <= capacity


def get_max_knapsack_profit(knapsack_capacity, weights, profits):
    item_count = len(profits)
    dp_table = create_dp_table(knapsack_capacity, item_count)

    # Build dp_table in bottom up manner
    for item_i in range(item_count + 1):
        for capacity in range(knapsack_capacity + 1):

            # profit is zero if capacity or item index is zero (ie. no items)
            if item_i == 0 or capacity == 0:
                dp_table[item_i][capacity] = 0

            if item_can_fit_knapsack(weights, item_i, capacity):
                profit_without_new_item = get_profit_without_new_item(
                    dp_table, item_i, capacity)
                profit_with_new_item = get_profit_with_new_item(
                    dp_table, profits, item_i, capacity, weights)

                dp_table[item_i][capacity] = max(
                    profit_with_new_item, profit_without_new_item)
            else:
                dp_table[item_i][capacity] = get_profit_without_new_item(
                    dp_table, item_i, capacity)

    return dp_table[item_count][knapsack_capacity]


profits = [60, 100, 120]
weights = [10, 20, 30]
knapsack_capacity = 50
print(get_max_knapsack_profit(knapsack_capacity, weights, profits))
# print(create_dp_table(knapsack_capacity, len(items)))
