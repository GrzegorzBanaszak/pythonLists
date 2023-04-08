def compare_numbers(number1, number2, number3):
    if number1 == number2 and number1 == number3 and number2 == number3:
        print("Liczby są sobie równe")
    else:
        biggest_number = 0
        for i in [number1, number2, number3]:
            if biggest_number < i:
                biggest_number = i

        print(f"Największa liczba to {biggest_number}")


compare_numbers(2, 2, 2)
compare_numbers(3, 4, 5)
compare_numbers(1, 34, 20)
