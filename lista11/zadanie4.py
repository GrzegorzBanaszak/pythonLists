
def inch_to_metric(value):
    cm = value * 2.54
    m = cm / 100
    km = m / 1000
    mm = cm * 10

    print(f"{value} cali to {mm} mm, {cm} cm, {m} m i {km} km")


def feets_to_metric(value):
    cm = value * 30.48
    m = cm / 100
    km = m / 1000
    mm = cm * 10

    print(f"{value} stóp to {mm} mm, {cm} cm, {m} m i {km} km")


inch_to_metric(1)
feets_to_metric(1)
