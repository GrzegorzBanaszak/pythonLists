def is_primary(number):
    i = 2
    while (i < number):
        if number % i == 0:
            return False
        i += 1

    return True


print(is_primary(5))
print(is_primary(6))
print(is_primary(7))
