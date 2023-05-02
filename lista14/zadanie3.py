import math


class Figura:
    fild = 0
    circuit = 0

    def show_fild(self):
        print(f"Pole wynosi {self.fild}")

    def show_circuit(self):
        print(f"Obwód wynosi {self.circuit}")

    def calculate_fild(self):
        self.show_fild()

    def calculate_circumference(self):
        self.show_circuit()


class Square(Figura):
    def __init__(self) -> None:
        super().__init__()

    def calculate_fild(self, side):
        self.fild = side ** 2
        return super().calculate_fild()

    def calculate_circumference(self, side):
        self.circuit = 4 * side
        return super().calculate_circumference()


class Rectangle(Figura):
    def __init__(self) -> None:
        super().__init__()

    def calculate_fild(self, sideA, sideB):
        self.fild = sideA * sideB
        return super().calculate_fild()

    def calculate_circumference(self, sideA, sideB):
        self.circuit = 2 * sideA + 2 * sideB
        return super().calculate_circumference()


class Triangle(Figura):
    def __init__(self) -> None:
        super().__init__()

    def calculate_fild(self, sideA, sideB):
        self.fild = (sideA * sideB) / 2
        return super().calculate_fild()

    def calculate_circumference(self, sideA, sideB, sideC):
        self.circuit = sideA + sideB + sideC
        return super().calculate_circumference()


class Circle(Figura):
    def __init__(self) -> None:
        super().__init__()

    def calculate_fild(self, radius):
        self.fild = math.pi * (radius ** 2)
        return super().calculate_fild()

    def calculate_circumference(self, radius):
        self.circuit = 2 * math.pi * radius
        return super().calculate_circumference()


class Rhombus(Figura):
    def __init__(self) -> None:
        super().__init__()

    def calculate_fild(self, diagonalA, diagonalB):
        self.fild = (diagonalA * diagonalB) / 2
        return super().calculate_fild()

    def calculate_circumference(self, sideA):
        self.circuit = 4 * sideA
        return super().calculate_circumference()


class Rhombus(Figura):
    def __init__(self) -> None:
        super().__init__()

    def calculate_fild(self, diagonalA, diagonalB):
        self.fild = (diagonalA * diagonalB) / 2
        return super().calculate_fild()

    def calculate_circumference(self, sideA):
        self.circuit = 4 * sideA
        return super().calculate_circumference()


class Trapeze(Figura):
    def __init__(self) -> None:
        super().__init__()

    def calculate_fild(self, sideA, sideB, height):
        self.fild = ((sideA + sideB)*height) / 2
        return super().calculate_fild()

    def calculate_circumference(self, sideA, sideB, sideC, sideD):
        self.circuit = sideA + sideB + sideC + sideD
        return super().calculate_circumference()


s1 = Square()
s1.calculate_fild(4)
s1.calculate_circumference(32)

s2 = Rectangle()
s2.calculate_circumference(3, 2)
