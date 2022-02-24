"""
A = [first, second]

if first is larger than second, first for B should be the largets possible value
If first is smaller than second, first for B should be the smallest possible value
if first is equal to the second, look at the third. If the third is equal to the second, look till n.
"""


def get_biggest_difference(num_list):
    diff_from_one = abs(num_list[1] - 1)
    diff_from_previous_num = abs(num_list[0] - num_list[1])
    return max(diff_from_one, diff_from_previous_num)


def generate_a(b):
    ans = 0

    first_index = 0
    second_index = 1

    while second_index <= len(b)-1:
        ans += get_biggest_difference([b[first_index], b[second_index]])

        first_index += 1
        second_index += 1

    return ans


b = [5, 5, 5, 100]
print(generate_a(b))
