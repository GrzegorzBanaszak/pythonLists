from math import floor


def celsius_to_fahrenheit(value):
    fahrenheit = (value * 9/5) + 32
    print(fahrenheit)

    if fahrenheit <= 32:
        print("Woda zamarza")

    if fahrenheit >= 212:
        print("Woda wrze")


def kelvin_to_fahrenheit(value):
    print(floor((value - 273.15) * 9/5 + 32))


def fahrenheit_to_kelvin(value):
    print(floor((value - 32) * 5/9 + 273.15))


def kelvin_to_celsius(value):
    print(floor(value - 273.15))


celsius_to_fahrenheit(100)
kelvin_to_fahrenheit(100)
fahrenheit_to_kelvin(100)
kelvin_to_celsius(100)
