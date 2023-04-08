import random


def get_user_input(type):
    user_input = None

    if type == "1":
        user_input = int(input("Podaj wartość całkowita: "))
    elif type == "2":
        user_input = float(input("Podaj wartość zmienno przecinkową: "))
    elif type == "3":
        user_input = random.randint(1, 100)

    return user_input


def get_average(arr):
    total = 0
    for i in arr:
        total += i

    return total / len(arr)


def get_key():
    key = None
    while True:
        key = input(
            "Podaj liczbę: \n 1.Całkowita \n 2.Zmienno przecinkową \n 3.Losową całkowitą \n")
        if key == "1" or key == "2" or key == "3":
            break

    return key


user_numbers = []

while True:
    key = get_key()
    userInput = get_user_input(key)
    user_numbers.append(userInput)
    isContinue = input("Chcesz podać jeszcze jakieś liczby? y/n ")
    if isContinue == "y":
        continue
    else:
        break

print(f"Średnia liczb {user_numbers} to {get_average(user_numbers)}")
