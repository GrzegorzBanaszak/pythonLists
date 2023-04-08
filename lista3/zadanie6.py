def print_stars(printNumber):
    stars = ""
    for i in range(printNumber):
        stars += "*"
    print(stars)


for i in range(1, 6):
    print_stars(i)
