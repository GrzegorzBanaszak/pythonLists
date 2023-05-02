class Vehicle:
    boardNumber = ""

    def __init__(self, boardNumber, type) -> None:
        self.boardNumber = boardNumber
        self.type = type

    def speed_up(self):
        print(self.type+" przyśpiesza")

    def __del__(self):
        print(f"Wyrejstrowanie: {self.boardNumber}")


class Car (Vehicle):

    def __init__(self, boardNumber) -> None:
        super().__init__(boardNumber, "Samochód")


class Motorcycle:
    def __init__(self, boardNumber) -> None:
        super().__init__(boardNumber, "Motocykl")


car1 = Car(34567)

car1.speed_up()
