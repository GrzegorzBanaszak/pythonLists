def is_it_divisible(number1, number2):
    is_divisible = int(number1) % int(number2) == 0

    if is_divisible:
        print(f"Liczba {number1} jest podzielna przez {number2}")
    else:
        print(f"Liczba {number1} nie jest podzielna przez {number2}")


number = input("Podaj liczbę:")
divider = input("Podaj dzielnik:")

is_it_divisible(number, divider)
