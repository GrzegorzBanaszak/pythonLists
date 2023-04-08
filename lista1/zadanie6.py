def get_speed(distance, time):
    return (distance / time) * 60


firstSpeed = get_speed(30, 15)
secondSpeed = get_speed(30, 12)


print(
    f"Pojazd poruszał sie z prędkościa {firstSpeed} i {secondSpeed} a jego średnia prędkość wynośi {(firstSpeed + secondSpeed)/2}")
