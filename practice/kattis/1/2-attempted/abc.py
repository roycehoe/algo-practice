"""https://open.kattis.com/problems/abc"""

a, b, c = input("").split()
a = int(a)
b = int(b)
c = int(c)

nums = [a, b, c]
nums.sort()
dict = {'A': nums[0], 'B': nums[1], 'C': nums[2]}

alphabets = input("")


print(
    f'{dict.get(alphabets[0])} {dict.get(alphabets[1])} {dict.get(alphabets[2])}')
