import random


def draw_number():
    return random.randint(1, 42)


def multi_lotto():
    numbers = []
    for i in range(5):
        is_currect = False
        while (is_currect == False):
            random_number = draw_number()
            if random_number not in numbers:
                numbers.append(random_number)
                is_currect = True
    print(numbers)


multi_lotto()
