import random


def generate_random_array(lenght, first, last):
    arr = []
    for i in range(lenght):
        arr.append(random.randint(first, last))

    return arr


lenghtOfFirstArr = int(input("Podaj długość listy: "))

while True:
    firstRandomNumber = int(input("Podaj poczatek lostowych liczb: "))
    lastRandomNumber = int(input("Podaj koniec losowych liczb: "))
    if firstRandomNumber < lastRandomNumber:
        break
    else:
        print("Końcowa liczba musi być większa niż pierwsza")
        continue


arr1 = generate_random_array(
    lenghtOfFirstArr, firstRandomNumber, lastRandomNumber)

print(arr1[len(arr1) - 3])

elementToRemove = int(input("Podaj element od końca do usunięcia: "))

arr1.pop(- elementToRemove)

arr2 = generate_random_array(10, firstRandomNumber, lastRandomNumber)


arr1 += arr2

noDuplicatedArr = set(arr1)
dictArr = {}

if len(noDuplicatedArr) != len(arr1):
    for i in arr1:
        if i not in dictArr:
            dictArr[i] = 1
        else:
            dictArr[i] = dictArr[i] + 1
    print(
        f"Długość połączonych list to {len(arr1)} a powtarzające się liczby {dictArr}")
else:
    print(
        f"Długość połączonych list to {len(arr1)} i nie ma powtarzających się liczb")
