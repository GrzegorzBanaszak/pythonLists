def is_rectangular(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("Trójkat o podanych bokach jest prostokatny")
    else:
        print("Trójkat o podanych bokach nie jest prostokatny")


is_rectangular(3, 4, 5)
is_rectangular(2, 3, 4)
