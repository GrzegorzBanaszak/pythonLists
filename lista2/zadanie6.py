def get_biggest(num1, num2, num3, num4):
    biggest = 0
    for i in [num1, num2, num3, num4]:
        if biggest < i:
            biggest = i
    print(f"Największa liczba to {biggest}")


get_biggest(205, 5, 1, 45)
