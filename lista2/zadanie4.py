def is_divisible_by_two(number):
    is_divisible = number % 2 == 0

    if is_divisible:
        return "i podzielna przez 2"
    else:
        return "nie podzielna przez 2"


def is_negative_or_positive(number):
    if number < 0:
        print(f"Liczba {number} jest ujemna {is_divisible_by_two(number)}")
    elif number > 0:
        print(f"Liczba {number} jest dodatnia {is_divisible_by_two(number)}")
    else:
        print(f"Liczba {number} jest rowna 0")


is_negative_or_positive(2)
is_negative_or_positive(-12)
is_negative_or_positive(3)
is_negative_or_positive(4)
