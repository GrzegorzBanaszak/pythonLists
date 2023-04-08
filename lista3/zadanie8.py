currentNumber = 0

for i in range(1, 1001):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        currentNumber = i


print(currentNumber)
