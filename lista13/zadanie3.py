class Screen:
    def __init__(self) -> None:
        pass

    def display(self):
        print("Wyświetlaj ...")

    def touch_screen(self):
        print("Zwróć miejsce wyświetlenia")


class Speaker:

    def __init__(self) -> None:
        pass

    def play_music(self):
        print("Odtwarzaj dzwięk")


class Microfon():
    def __init__(self) -> None:
        pass

    def record(self):
        print("Nagrywaj głos")


class Smarthphone:
    def __init__(self) -> None:
        self.phoneScreen = Screen()
        self.phoneSpeaker = Speaker()
        self.phoneMicrofon = Microfon()

    def phone_calls(self):
        self.phoneMicrofon.record()
        self.phoneSpeaker.play_music()
        self.phoneScreen.display()


phone = Smarthphone()
phone.phone_calls()
