import random


def draw_number():
    return random.randint(1, 49)


def lotto():
    numbers = []
    for i in range(6):
        is_currect = False
        while (is_currect == False):
            random_number = draw_number()
            if random_number not in numbers:
                numbers.append(random_number)
                is_currect = True
    print(numbers)


lotto()
