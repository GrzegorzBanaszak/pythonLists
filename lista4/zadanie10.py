prevNumber = []
total = 0
while True:
    num = int(input("Podaj liczbę: "))
    total += num
    if prevNumber == num:
        break
    else:
        prevNumber = num
