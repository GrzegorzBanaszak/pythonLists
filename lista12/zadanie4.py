wysokosc = 0
bezpieczna_wysokosc = 5000


while True:
    try:
        wysokosc = int(input("Na jakiej wysokości lecimy? [w metrach]: "))
        break
    except ValueError:
        print("Błędna wartość. Podaj liczbę.")


# Sprawdzenie wartości wysokości
if wysokosc < bezpieczna_wysokosc:
    print(f"{wysokosc / 1000} km to za nisko!")
else:
    print("Na tej wysokości jesteś już bezpieczny.")
