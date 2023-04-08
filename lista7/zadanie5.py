tur1 = ("kolej", "najlepszy")
tur2 = ("jelok", "jeśli pan")

for text1, text2 in zip(tur1, tur2):
    text1_set = set(text1)
    text2_set = set(text2)
    if text1_set == text2_set:
        print(f"{text1} i {text2} to anagramy!")
    else:
        print(f"{text1} i {text2} to nie anagramy.")
