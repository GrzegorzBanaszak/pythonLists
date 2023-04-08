tup = ("1", "2", "3", 4, 5, 6)

print(len(tup))
print(id(tup))

tup = tup + ("7", 8)

print(tup)

print(id(tup))

arr = list(tup)

print(arr)
