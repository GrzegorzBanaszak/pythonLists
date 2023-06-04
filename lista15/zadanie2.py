class Beer:
    def __init__(self, name, category, percentageConcentration, price, opinion) -> None:
        self.name = name
        self.category = category
        self.percentageConcentration = percentageConcentration
        self.price = price
        self.opinion = opinion

    def __str__(self) -> str:
        return f"{self.name} {self.category} {self.price}"


class Shop:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sort_by_price(self):
        self.products.sort(key=lambda x: x.price)

    def display_products(self):
        for product in self.products:
            print(product)


shop = Shop()
shop.add_product(Beer("Piwo XZ", "Jasne", "3.5", 5, "Good beer"))
shop.add_product(Beer("Piwo XC", "Jasne", "3.5", 6.4, "Good beer"))
shop.add_product(Beer("Piwo DX", "Jasne", "3.5", 3.4, "Good beer"))
shop.sort_by_price()
shop.display_products()
