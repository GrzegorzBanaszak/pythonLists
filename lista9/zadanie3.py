set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([4, 5, 6, 7, 8, 9])

print(len(set1))
print(len(set2))

set1.discard(3)
set2.discard(9)

print(set1.intersection(set2))
print(set1.difference(set2))

# Dzieki konwersji na liste możemy odwołaś się do indeksu
print(list(set1))
