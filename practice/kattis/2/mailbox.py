"""https://open.kattis.com/problems/mailbox"""

"""
m is how many firecrackers the mailbox can withstand

Test at 50.
    If blow up, m is < 50
        Test at 25
        if blow up
            m is < 25
        else:
            m is 25 to 50
    If no blow up, m is >= 50



"""

# n = int(input(''))
# data = []

# for i in range(0, n):
#     k, m = input('').split()
#     k = int(k)
#     m = int(m)
#     data.append({k, m})


from math import ceil, floor
k = 3
m = 73

upper = 100
lower = 1

ans = 0
guess = 0


def cannot_widstand(guess, m):
    return guess > m


while k != 1:
    print(guess)
    guess = ceil((upper + lower)/2)
    ans += guess

    if cannot_widstand(guess, m):
        upper = guess
        k -= 1
    else:
        lower = guess

print(guess)
