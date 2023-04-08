import math


def powers_of_two(n):
    for i in range(1, n+1):
        print(int(math.pow(2, i)))


powers_of_two(3)
powers_of_two(5)
