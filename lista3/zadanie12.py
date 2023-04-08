import random

eagleNumbers = 0
pileNumbers = 0

for i in range(50):
    result = random.randint(0, 1)
    if result == 0:
        eagleNumbers += 1
        print("Orzeł")
    else:
        pileNumbers += 1
        print("Reszka")


print(f"Wylosowano {eagleNumbers} razy orła i {pileNumbers} razy reszkę")
