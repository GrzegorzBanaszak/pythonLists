n = int(input("Podaj ilość liczb: "))
for i in range(n):
    liczba = int(input(f"Podaj {i+1}. liczbę: "))
    if liczba >= -6 and liczba <= 6:
        print("Liczba jest z przedziału [-6,6].")
    else:
        print("Liczba nie należy do przedziału [-6,6].")
