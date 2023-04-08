count = 0
prev_num = None
while True:
    num = int(input("Podaj liczbę: "))
    if prev_num is not None and abs(num - prev_num) < 5:
        break
    prev_num = num
    count += 1
print("Wczytano", count, "liczb do momentu, gdy wartość bezwzględna różnicy pomiędzy dwoma kolejnymi liczbami była mniejsza niż 5.")
