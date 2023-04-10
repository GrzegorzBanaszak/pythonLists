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

print("Zestaw 1:", set1)
print("Zestaw 2:", set2)
print("Zestaw 3:", set3)
print("Zestaw 4:", set4)
