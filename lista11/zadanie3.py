from math import floor, radians, sin, cos, tan


def get_trygo(value):

    angle = radians(value)

    print(f"Sinus kąta {value} wynosi: {round(sin(angle),2)}")
    print(f"Cosin kąta {value} wynosi: {round(cos(angle),2)}")
    print(f"Tangens kąta {value} wynosi: {round(tan(angle),2)}")
    print(
        f"Cotangens kąta {value} wynosi: {round(tan(1 / tan(angle)),2)}")


userInput = int(input("Podaj wielkosć kąta: "))


get_trygo(userInput)
get_trygo(70)
get_trygo(90)
get_trygo(35)
get_trygo(180)
get_trygo(240)
get_trygo(360)
