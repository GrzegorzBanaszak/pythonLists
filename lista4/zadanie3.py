isDivisibleBy12 = False

while (isDivisibleBy12 == False):
    input_number = int(input("Podaj liczbę:"))
    if input_number % 12 == 0:
        break


print("Podałeś liczbe podzielną przez 12")
