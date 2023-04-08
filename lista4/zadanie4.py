def get_number():
    user_input = input("Podaj liczbę liczbę: ")
    if user_input == 0 or user_input == "NULL" or user_input.isdigit() == False:
        return 0
    else:
        return int(user_input)


while (True):
    number1 = get_number()
    if number1 == 0:
        break
    number2 = get_number()
    if number2 == 0:
        break

    print(f"Średnia liczb {(number1+ number2) / 2}")
