import random


n = random.randint(0, 100)

sum_of_squares = sum([i ** 2 for i in range(n + 1)])


print(f"Suma kwadratów liczb od 0 do {n} wynosi: {sum_of_squares}")
