def check_your_sobriety(value):
    if value < 0.2:
        print("Jesteś trzeżwy")
    elif value > 0.2 and value < 0.5:
        print("Jesteś w stanie po spożyciu alkoholu")
    else:
        print("Jesteś w stanie nietrzeźwości")


check_your_sobriety(.1)
check_your_sobriety(.3)
check_your_sobriety(.6)
