def get_dividers(number):
    numbers = []
    for i in range(1, number):
        if number % i == 0:
            numbers.append(i)
    return numbers


def is_number_perfect(number):
    dividers = get_dividers(number)
    total = 0
    for i in dividers:
        total += i

    if total == number:
        return True
    else:
        return False


print(is_number_perfect(6))
print(is_number_perfect(7))
print(is_number_perfect(28))
