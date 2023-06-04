class Deck:
    cards = []

    def add_card(self, card):
        self.cards.append(card)

    def display_cards(self):
        for card in self.cards:
            card.display()

    def sort_deck(self):
        self.cards.sort(key=lambda card: card.type)

    def get_from_top(self):
        return self.cards.pop(0)

    def remove_card(self, type, color):
        self.cards = filter(lambda card: card.type !=
                            type and card.color != color, self.cards)


class Card:
    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color

    def __str__(self) -> str:
        return self.type

    def display(self):
        print(f"_____\n|{self.color}  |\n| {self.type} |\n|   |\n-----")

    def is_similar(self, card):
        if self.type == card.type and self.color == card.color:
            return True
        else:
            return False


deck = Deck()
deck.add_card(Card("A", "♣"))
deck.add_card(Card("K", "♥"))
deck.add_card(Card("K", "♠"))
deck.add_card(Card("1", "♣"))

print(deck.cards[1].is_similar(deck.cards[2]))

print(deck.get_from_top())
deck.sort_deck()
deck.display_cards()
