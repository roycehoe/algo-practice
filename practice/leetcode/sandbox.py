"""
Possible ans is itself or 2
"""


card_arr = [3, 8, 7, 6, 4]



def get_shifts(card_arr, factor):
    ans = 0
    for i in card_arr:
        if not i % factor:
            ans += 1

    return ans

def main(card_arr):
    ans = get_shifts(card_arr, 2)
    for i in card_arr


print(get_default_ans(card_arr))