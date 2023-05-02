class Animal:
    def __init__(self, type, weight, legs) -> None:
        self.type = type
        self.weight = weight
        self.legs = legs


class Dog(Animal):
    def __init__(self, weight) -> None:
        super().__init__("Ssak", weight, 4)

    def give_voice(self):
        print("Hou hou")


class Cat(Animal):
    def __init__(self, weight) -> None:
        super().__init__("Ssak", weight, 4)

    def give_voice(self):
        print("Miou")


class Bird(Animal):
    def __init__(self, weight) -> None:
        super().__init__("Ptaki", weight, 2)

    def fly(self):
        print("I fly")


class Fish(Animal):
    def __init__(self, type, weight) -> None:
        super().__init__(type, weight, 0)

    def swim():
        print("I swim underwater")
