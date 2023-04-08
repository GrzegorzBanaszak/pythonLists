numbers = []
while True:
    n = int(input("Podaj początek zakresu: "))
    x = int(input("Podaj koniec zakresu: "))
    if n == 0 or x == 0:
        print("Program zakończony.")
        break
    for num in range(n, x):
        if len(numbers) >= 6:
            break
        numbers.append(num)
    print("Liczby:", numbers)
    print("Minimum:", min(numbers))
    print("Maksimum:", max(numbers))
    print("Średnia:", sum(numbers)/len(numbers))
    sorted_numbers = sorted(numbers)
    middle_index = len(numbers) // 2
    median = sorted_numbers[middle_index] if len(numbers) % 2 == 1 else (
        sorted_numbers[middle_index-1] + sorted_numbers[middle_index]) / 2
    print("Mediana:", median)
    numbers = []
