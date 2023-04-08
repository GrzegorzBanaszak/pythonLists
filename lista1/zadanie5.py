def convert_inch_to_cm(inch):
    return float(inch) * 2.54


inchValue = input("Podaj wartość do konwersji: ")


print(f"{inchValue} cali to {convert_inch_to_cm(inchValue)} centymetrów")
