import random


def generate_random_array(lenght):
    arr = []
    for i in range(lenght):
        arr.append(random.randint(1, 50))

    return arr


arr = generate_random_array(10)

print(arr)

random.shuffle(arr)

print(arr)

arr.sort()

print(arr)

arr.sort(reverse=True)

print(arr)
