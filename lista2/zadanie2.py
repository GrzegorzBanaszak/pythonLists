def check_number(number):
    if number <= 10:
        print("Liczba jest mniejsza bądz równa 10")
    elif number >= 10 and number <= 25:
        print("Liczba jest większa bądz równa 10 lecz mniejsza od 25")
    else:
        print("Liczba jest większa od 25")


check_number(1)
check_number(12)
check_number(40)
