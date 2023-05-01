class Car:
    def __init__(self, mark, model, value, color) -> None:
        self.mark = mark
        self.model = model
        self.mileage = 0
        self.value = value
        self.color = color

    def __str__(self) -> str:
        return f"{self.mark} - {self.model} | Kolor - {self.color} | Przebieg - {self.mileage} | Wartość - {self.value}"

    def speed_up(self):
        self.speed += 10
        self.mileage += 10

    def slow(self):
        if (self.speed > 0):
            self.speed -= 10

    def show_speed(self):
        print(f"{self.speed} km/h")

    def dye_car(self, newColor):
        self.color = newColor

    def sell_car(self):
        return self.value / (self.mileage / 2)


car1 = Car("Ferrari", "kabriolet", 60000, "Czerwony")
car2 = Car("Ford", "sedan", 45000, "Niebieski")

print(car1)
print(car2)
