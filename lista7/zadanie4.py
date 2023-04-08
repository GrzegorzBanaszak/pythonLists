tur = ("a", "b", "c", "d", "e", "f")


for i in tur:
    if i in "Hello":
        print(tur.index(i))


shortText = "Dzisiaj jest piękna pogoda. Słońce świeci, ptaki śpiewają, a w powietrzu unosi się zapach wiosny."

user_input = input("Podaj słowo: ")


if user_input in shortText:
    print(shortText.count(user_input))
