n = int(input("Podaj liczbę: "))
arr = []

for i in range(n, 1, -1):
    if n % i == 0:
        arr.append(i)


print(f"Liczby podzielne przez {n} to: {arr}")
