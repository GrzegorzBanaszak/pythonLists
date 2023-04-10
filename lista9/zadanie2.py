import random

teamsPool = ["Real Madrid", "Barcelona", "PSG", "Bayern Monachium", "Liverpool", "Manchester City", "Manchester United", "Chelsea", "Tottenham Hotspur",
             "Arsenal", "Juventus", "AC Milan", "Inter Milan", "Napoli", "AS Roma", "Ajax Amsterdam", "Benfica", "FC Porto", "Galatasaray", "Fenerbahce"]


def drawn_teams():
    teams = set()
    while True:
        if len(teams) == 10:
            break
        else:
            teams.add(random.choice(teamsPool))
    return teams


set1 = drawn_teams()
set2 = drawn_teams()
set3 = drawn_teams()
set4 = drawn_teams()

set1.intersection(set2)
set1.issuperset(set2)
set1.difference(set3)
set1.issubset(set3)
set1.union(set4)


# Wyciąganie inforamcji z listy za pomoca pętli i konwersji na listę
for i in set1:
    print(i)

print(list(set1)[1])
