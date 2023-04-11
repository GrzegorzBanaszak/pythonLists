
text1 = "Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'."
slice = text1[:text1.index('.') + 1]

print(slice)


words = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."]
text2 = ' '.join(words)
text2 = text2.replace(" .", ".")
