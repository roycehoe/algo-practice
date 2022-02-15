"""https://open.kattis.com/problems/hothike"""

n = int(input(""))
t_list = input("").split()
t_list = [int(i) for i in t_list]


best_hike = {
    "max_temp": 100,
    "day_to_start": 0
}


for i in range(0, len(t_list)-2):
    temp_range = [t_list[i], t_list[i+2]]
    if max(temp_range) < best_hike.get("max_temp"):
        best_hike["max_temp"] = max(temp_range)
        best_hike["day_to_start"] = i+1

print(f'{best_hike.get("day_to_start")} {best_hike.get("max_temp")} ')
