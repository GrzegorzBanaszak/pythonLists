class Book:
    def __init__(self, name, author, price, pages, publishing) -> None:
        self.name = name
        self.author = author
        self.price = price
        self.pages = pages
        self.publishing = publishing
        self.readed_pages = 0

    def __repr__(self) -> str:
        return "{ " + self.name + " }"

    def read(self, pages):
        self.readed_pages = pages

    def sell_book(self):
        return self.price

    def how_many_to_read(self):
        print(f"Do przeczytania pozostało {self.pages - self.readed_pages}")

    def lend(self):
        print(f"Porzyczyłeść książkę {self.name}")

    def read_again(self):
        self.readed_pages = 0


books = [Book("Książka 33", "Autor 3", 43, 300, "Wydawnictwo 2"),
         Book("Książka 12", "Autor 1", 20, 200, "Wydawnictwo 1"),
         Book("Książka 2", "Autor 2", 24, 210, "Wydawnictwo 1"),
         Book("Książka 56", "Autor 4", 30, 280, "Wydawnictwo 5"),
         Book("Książka 45", "Autor 5", 22, 190, "Wydawnictwo 3"),
         ]


books.sort(key=lambda book: book.name)

print(books)
