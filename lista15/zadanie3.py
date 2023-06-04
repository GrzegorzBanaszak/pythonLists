class Citizen:
    def __init__(self, firstName, lastName, street, houseNumber, zipCode, place) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.street = street
        self.houseNumber = houseNumber
        self.zipCode = zipCode
        self.place = place

    def format(self):
        return f"----------------------\n{self.firstName} {self.lastName}\n{self.street} {self.houseNumber}\n{self.zipCode} {self.place}\n----------------------\n"

    def save_to_file(self):
        file = open(f"{self.firstName}{self.lastName}.txt", "a")
        file.write(self.format())
        file.close()


person = Citizen("Jan", "Kowalski", "ul. Rakowiecka", 20, "00-001", "Warszawa")
person.save_to_file()
