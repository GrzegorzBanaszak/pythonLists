import math


fildsSum = 0

for i in range(1, 101):
    fildsSum += 6 * i**2

print(fildsSum)

total = 0
powerOfSix = math.pow(10, 6)
number = 1
while True:
    if total >= powerOfSix:
        break
    total += number
    number += 1

print(total, number)
