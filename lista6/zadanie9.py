arr = []

for i in range(5):
    user_input = int(input("Podaj liczbę: "))
    arr.append(user_input)


arr.sort(reverse=True)

occurrenceTheLargestNumber = 0

for i in range(len(arr)):
    if arr[0] == arr[i]:
        occurrenceTheLargestNumber += 1
    else:
        break


print(
    f"Największa liczba to {arr[0]} i występuje {occurrenceTheLargestNumber} razy")
