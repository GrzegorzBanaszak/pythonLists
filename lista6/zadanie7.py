import random


def draw_number():
    return random.randint(1, 49)


def get_user_numbers():
    numbers = []
    for i in range(6):
        while True:
            user_number = int(input(f"Podaj {i + 1} liczbę: "))
            if user_number not in numbers and user_number < 50:
                numbers.append(user_number)
                print(f"Aktualnie wybrane liczby {numbers}")
                break
            else:
                print("Wybrałęś już tą liczbe lub liczba jest większa niż 49")
                print(f"Aktualnie wybrane liczby {numbers}")
                continue
    return numbers


def lotto():
    numbers = []
    for i in range(6):
        while True:
            random_number = draw_number()
            if random_number not in numbers:
                numbers.append(random_number)
                break

    return numbers


def hit_or_miss():
    numbers = []
    for i in range(6):
        while True:
            random_number = draw_number()
            if random_number not in numbers:
                numbers.append(random_number)
                break

    return numbers


def check_win(user_numbers, lotto_numbers):
    hit_numbers = 0
    for i in user_numbers:
        if i in lotto_numbers:
            hit_numbers += 1

    print(hit_numbers)
    if hit_numbers == 6:
        print(f"Wygrałeś 1 000 000 zł")
    elif hit_numbers == 5:
        print(f"Wygrałeś 3 500 zł")
    elif hit_numbers == 4:
        print(f"Wygrałeś 100 zł")
    elif hit_numbers == 3:
        print(f"Wygrałeś 10 zł")
    else:
        print(f"Spróbuj następnym razem")


userNumbers = hit_or_miss()

lottoNumbers = lotto()


check_win(userNumbers, lottoNumbers)
