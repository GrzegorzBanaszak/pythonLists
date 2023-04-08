import random


numberToGuess = random.randint(1, 100)
chance = 3

while True:
    guess = int(input("Zgadnij liczbę od 1-100: "))
    chance -= 1
    if guess == numberToGuess:
        print("Podałeś prawidłową liczbę")
        break
    elif chance > 0 and guess > numberToGuess:
        print(f"Podałeś za dużą wartość i pozostało ci {chance} szans")
        continue
    elif chance > 0 and guess < numberToGuess:
        print(f"Podałeś za mało wartość i pozostało ci {chance} szans")
        continue
    else:
        print("Haha przegrałeś")
        break
