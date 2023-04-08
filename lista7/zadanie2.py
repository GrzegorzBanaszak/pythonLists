import random


def generate_random_array(lenght):
    arr = []
    for i in range(lenght):
        arr.append(random.randint(0, 10))

    return arr


tup = tuple(generate_random_array(100))

numberZero = 0
numberOne = 0
numberTwo = 0

for i in tup:
    if i == 0:
        numberZero += 1
    elif i == 1:
        numberOne += 1
    elif i == 2:
        numberTwo += 1

print(
    f"W krotce znajduje się {numberZero} zer, {numberOne} jedynek i {numberTwo} dwójek")

for i in tup:
    if i % 2 == 0:
        print(f"Liczba {i} jest parzysta")
    else:
        print(f"Liczba {i} jest nie parzysta")
