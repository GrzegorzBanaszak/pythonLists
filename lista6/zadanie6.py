import random


def generate_random_array(lenght, first, last):
    arr = []
    for i in range(lenght):
        arr.append(random.randint(first, last))

    return arr


arr1 = generate_random_array(20, 1, 6)


noDuplicatedArr = set(arr1)


print(
    f"Pozostałe liczby to {noDuplicatedArr} a długość listy to {len(noDuplicatedArr)}")
