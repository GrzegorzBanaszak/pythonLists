def feets_to_metric(value):
    cm = value * 30.48
    m = cm / 100
    km = m / 1000
    mm = cm * 10

    return [mm, cm, m, km]


print(feets_to_metric(2))
