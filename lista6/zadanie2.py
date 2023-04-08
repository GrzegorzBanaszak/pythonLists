arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(0, 10, 3):
    if i == len(arr) - 1:
        print(arr[i - 1])
    else:
        print(arr[i])
