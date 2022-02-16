"""https://open.kattis.com/problems/doorman"""

x = int(input(""))
queue = [i for i in input("")]
table = {'M': 1, 'W': -1}

ans = 0
gender_dif = 0

while len(queue) > 0:
    next_person = queue.pop(0)
    gender_dif += table.get(next_person)
    if gender_dif > x:
        break
    ans += 1

print(ans)
