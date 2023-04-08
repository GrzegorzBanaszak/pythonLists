arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


for i in range(0, 10, 3):
    if i == len(arr) - 1:
        print(arr[i - 1])
    else:
        print(arr[i])
