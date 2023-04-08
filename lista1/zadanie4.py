from datetime import datetime

secondsPerMinutes = 60
secondsPerHoures = 60 * secondsPerMinutes
secondsPerDay = secondsPerHoures * 24
secondsPerYear = secondsPerDay * 365


print(
    f"Ilość sekund która mieści się w godzinie: {secondsPerHoures},dniu: {secondsPerDay} i roku: {secondsPerYear}")


todayDay = datetime.today()
dateOfBirth = datetime(1995, 3, 17)


print(
    f"Ilość sekund od urodzenia {int(todayDay.timestamp() - dateOfBirth.timestamp())}")
