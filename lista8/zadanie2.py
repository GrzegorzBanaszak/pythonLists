bookOfContact = {"Carlita": "273 114 6454", "Arman": "692 991 0329", "Lissie": "904 392 3245", "Cazzie": "606 407 6287",
                 "Sharona": "746 767 1501", "Wilie": "544 806 5892", "Evanne": "239 767 6776", "Trixy": "457 624 9376", "Stevie": "121 444 0194", "Franklin": "663 156 8691"}

bookOfContact["Carlita"] = "123 456 789"
bookOfContact["Franklin"] = "987 654 321"

bookOfContact.pop("Sharona")

# print(bookOfContact)

bookOfContact.clear()

bookOfContact["Elayne"] = "105 804 2519"
bookOfContact["Danielle"] = "203 359 6679"

booksKeys = list(bookOfContact.keys())

booksKeys.sort()

bookOfContact = {i: bookOfContact[i] for i in booksKeys}

print(bookOfContact)
