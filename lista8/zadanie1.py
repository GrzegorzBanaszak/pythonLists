menu = {"Hawajska": 19.90, "Fungi": 21.90, "Margherita": 18.00, "Salami": 20,
        "Pollo": 21.90, "Vege": 21.00, "Simple": 23.00, "Texas": 25, "Latina": 24, "Parma": 28}


def add_new_pizza(name, price):
    menu.update({name: price})


add_new_pizza("Mięsna", 30)

for value in menu.values():
    print(f"Wartość {value}")

for key in menu.keys():
    print(f"Klucz {key}")


for key, value in menu.items():
    print(f"{key}:{value} zł")
