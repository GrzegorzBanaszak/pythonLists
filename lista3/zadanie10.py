import random


def draw_number():
    return random.randint(1, 80)


def multi_multi():
    numbers = []
    for i in range(20):
        is_currect = False
        while (is_currect == False):
            random_number = draw_number()
            if random_number not in numbers:
                numbers.append(random_number)
                is_currect = True
    print(numbers)


multi_multi()
