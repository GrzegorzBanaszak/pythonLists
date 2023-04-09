users = {"admin": "password", "Tiphany": "Tiphany123", "Chadwick": "Chadwick123",
         "Dasha": "Dasha123",
         "Reider": "Reider123",
         "Jarret": "Jarret123", }


def login():

    while True:
        userName = input("Podaj nazwę: ")
        userPassword = input("Podaj hasło: ")

        if userName in users.keys() and users[userName] == userPassword:
            if userName == "admin":
                print("Wyświetl login admina")
                break
            else:
                print("Wyswietl strone")
                break
        else:
            print("Nie poprawny login bądz hasło")
            continue


login()
