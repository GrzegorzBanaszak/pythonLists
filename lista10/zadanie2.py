class Person:
    def __init__(self, firstName, lastName, phoneNumber, shoes) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.shoes = shoes
        self.validation_name()
        self.name_begin_uppercase()
        self.validate_phone()
        self.validate_shoes()
        self.is_female()

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName} {self.phoneNumber} - {self.shoes}"

    def validation_name(self):
        if self.firstName.isalpha() and self.lastName.isalpha():
            return True
        else:
            self.firstName
            return False

    def name_begin_uppercase(self):
        if self.firstName.isupper() and self.lastName.isupper():
            return True
        else:
            self.firstName = self.firstName.capitalize()
            self.lastName = self.lastName.capitalize()
            return False

    def validate_phone(self):
        if self.phoneNumber.isnumeric():
            self.phoneNumber = ''.join(
                char for char in self.phoneNumber if char.isalnum() or char.isspace())
            return True
        else:
            self.phoneNumber = ''.join(
                char for char in self.phoneNumber if char.isalnum() or char.isspace())
            return False

    def validate_shoes(self):
        if self.shoes.isnumeric():
            self.shoes = ''.join(
                char for char in self.shoes if char.isalnum() or char.isspace())
            return True
        else:
            self.shoes = ''.join(
                char for char in self.shoes if char.isalnum() or char.isspace())
            return False

    def is_female(self):
        female_names = ["Anna", "Maria",
                        "Małgorzata", "Katarzyna", "Agnieszka"]
        for name in female_names:
            if self.firstName.lower() == name.lower():
                return True

        return False


firstName = input("Podaj imię: ")
lastName = input("Podaj nazwisko: ")
phone = input("Podaj numer telefonu: ")
shoes = input("Podaj numer buta: ")

person = Person(firstName, lastName, phone, shoes)

print(person)
