"""https://open.kattis.com/problems/coursescheduling"""


from collections import OrderedDict


n = int(input())

"""
If name and course never seen before, add name and course
If name seen before:
    if course and name never seen before
        add course
"""

applied = set()
ans = {}


def is_existing_dict_entry(dictionary, key):
    return False if dictionary.get(key) is None else True


def increment_course_count(dictionary, key):
    if is_existing_dict_entry(dictionary, key):
        temp = dictionary.get(key)
        temp += 1
        dictionary[key] = temp
    else:
        dictionary[key] = 1

    return dictionary


for i in range(0, n):
    fn, ln, course = input().split()
    name = fn + ln
    entry = name + course
    if entry not in applied:
        applied.add(entry)
        ans = increment_course_count(ans, course)

ans = {val[0]: val[1]
       for val in sorted(ans.items(), key=lambda x: (-x[1], x[0]))}

ans = OrderedDict(ans)


for k, v in ans.items():
    print(k, v)
