x = 0
y = 1
n = 6


def get_mod_fib(t1, t2, n):
    ans_list = [t1, t2]
    n = n - 2

    for i in range(n):
        last_num = ans_list[len(ans_list)-1]
        second_last_num = ans_list[len(ans_list) - 2]

        next_num = second_last_num + last_num**2
        ans_list.append(next_num)

    print(ans_list[len(ans_list)-1])


get_mod_fib(x, y, n)
