import random


def generate_random_array(lenght, type):
    arr = []
    if type == "odd":
        for i in range(lenght):
            arr.append(random.choice([2, 4, 6, 8, 10]))
    else:
        for i in range(lenght):
            arr.append(random.choice([1, 3, 5, 7, 9]))

    return arr


tupOdd = tuple(generate_random_array(100, "odd"))
tupEven = tuple(generate_random_array(100, "even"))

tup = tupOdd + tupEven

print(len(tup))

if 0 in tup:
    print("W krotce znajduje się 0")

if 100 in tup:
    print("W krotce znajduje się 100")

print(id(tup))
