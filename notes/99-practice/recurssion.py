def count_to_hundred(start):
    if start >= 100:  # break case
        return

    print(start)  # recursion case
    count_to_hundred(start+1)


def print_list(list):
    if list == []:
        return

    print(list.pop(0))
    print_list(list)
