def print_number(number):
    for i in range(number, -1, -1):
        if i % 6 == 0 and i % 9 == 0:
            print(i)


print_number(100)
