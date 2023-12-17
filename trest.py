list1 = [["Alice", 20, "math"]]
d1 = {}
for item in list1:
    key = item[0].lower()
    d1[key] = item
print(d1)

