import math


def quadratic_equation(a, b, c):
    delta = math.pow(b, 2) - (4 * a * c)

    if delta > 0:
        x1 = -b - math.sqrt(delta)/(2*a)
        x2 = -b + math.sqrt(delta)/(2*a)

        print(f"Rozwiązanie x1 ={x1}")
        print(f"Rozwiązanie x2 ={x2}")
    elif delta == 0:
        x = -b/(2*a)

        print(f"Rozwiązanie x ={x}")
    else:
        print("Brak rozwiązań")


quadratic_equation(1, 4, 2)
