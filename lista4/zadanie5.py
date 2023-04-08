numbers = []


def get_sum(arr_numbers):
    total = 0
    for i in arr_numbers:
        total += i
    return total


def get_averge(arr_numbers):
    total = get_sum(arr_numbers)
    return int(total / len(arr_numbers))


while (True):
    user_input = int(input("Podaj liczbę: "))
    numbers.append(user_input)
    total = get_sum(numbers)
    averge = get_averge(numbers)
    if total >= 100 or averge == 66:
        break
    print(f"Suma {total} i średnia {averge}")
