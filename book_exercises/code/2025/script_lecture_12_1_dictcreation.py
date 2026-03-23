import numpy as np

screentime = {"Mon": 8, "Tue": 10, "Wed": 12, "Thu": 3, "Fri": 6}

#print(screentime)
#print(screentime["Tue"])
#for k, v in screentime.items():
#    print(f"On {k} my screentime was: {v} hours")

#tot = np.sum(np.array(list(screentime.values())))
#print(f"The total screentime this week: {tot} hours")

screentime["Tue"] = 4
del screentime["Wed"]
for k, v in screentime.items():
    print(f"On {k} my screentime was: {v} hours")

names = ["Mary", "Joe", "Mehmet", "Julie", "Fethiye"]
count = {name: len(name) for name in names}
print(count)