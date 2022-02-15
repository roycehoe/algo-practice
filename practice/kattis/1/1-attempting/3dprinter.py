"""https://open.kattis.com/problems/3dprinter"""

"""
Statues
Printers
"""




import math
def get_days_to_build_statues(statue_count, machines):
    days_to_build_machines = machines - 1
    days_to_build_statues = math.ceil(statue_count / machines)
    return days_to_build_statues + days_to_build_machines


# def main(n):
#     min_days = n

#     for machine_building_days in range(1, n+1):
#         machines = 2**machine_building_days
#         ans = get_days_to_build_statues(n, machines)

#         if ans < min_days:
#             min_days = ans
#         else:
#             return min_days


# print(main(100))
n = int(input(""))

min_days = n

for machine_building_days in range(1, n+1):
    machines = 2**machine_building_days
    ans = get_days_to_build_statues(n, machines)

    if ans < min_days:
        min_days = ans

print(min_days)
