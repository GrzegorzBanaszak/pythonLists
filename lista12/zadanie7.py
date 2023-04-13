arr1 = {1: "I", 2: "II", 3: "III", 4: "IV",
        5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
arr2 = {1: "X", 2: "XX", 3: "XXX", 4: "XL",
        5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
arr3 = {1: "C", 2: "CC", 3: "CCC", 4: "CD",
        5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
arr4 = {1: "M", 2: "MM", 3: "MMM"}


def convert_to_roma(number):
    list_of_numbers = list(reversed([int(x) for x in str(number)]))
    rome_number = ""

    if len(list_of_numbers) >= 4 and list_of_numbers[3] > 0:
        rome_number += arr4[list_of_numbers[3]]

    if len(list_of_numbers) >= 3 and list_of_numbers[2] > 0:
        rome_number += arr3[list_of_numbers[2]]

    if len(list_of_numbers) >= 2 and list_of_numbers[1] > 0:
        rome_number += arr2[list_of_numbers[1]]

    rome_number += arr1[list_of_numbers[0]]

    return rome_number


def roma_to_number(roma_number):
    number = []
    selected = 0
    for key, val in arr1.items():
        if val in roma_number:
            selected = key

    number.append(selected)
    selected = 0

    for key, val in arr2.items():
        if val in roma_number:
            selected = key

    number.append(selected)
    selected = 0

    for key, val in arr3.items():
        if val in roma_number:
            selected = key

    number.append(selected)
    selected = 0

    for key, val in arr4.items():
        if val in roma_number:
            selected = key

    number.append(selected)

    number = list(reversed(number))

    number = [str(integer) for integer in number]

    return int("".join(number))


print(roma_to_number("MCMLXXXVII"))
print(convert_to_roma(1987))
