class Restaura:
    def __init__(self, name) -> None:
        self.name = name

    def display_menu(self):
        pass

    def add_to_menu(self, menuItem):
        pass


class IceCreamStand(Restaura):

    def __init__(self, name) -> None:
        self.flavors = []
        super().__init__(name)

    def display_menu(self):
        print(f"Lodziarnia {self.name} menu:")
        for menuItem in self.flavors:
            print(menuItem)

    def add_to_menu(self, menuItem):
        self.flavors.append(menuItem)


class CoffeeShop(Restaura):

    def __init__(self, name) -> None:
        self.coffee = []
        super().__init__(name)

    def display_menu(self):
        print(f"Kawiarnia {self.name} menu:")
        for menuItem in self.coffee:
            print(menuItem)

    def add_to_menu(self, menuItem):
        self.coffee.append(menuItem)


res1 = IceCreamStand("Lodzik")
res1.add_to_menu("Bananowe")
res1.add_to_menu("Waniliowe")
res1.add_to_menu("Czekoladowe")
res1.display_menu()


res2 = CoffeeShop("Czarna")
res2.add_to_menu("Espresso")
res2.add_to_menu("Ristretto")
res2.add_to_menu("Americano")
res2.display_menu()
