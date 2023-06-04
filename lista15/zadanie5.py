class Room:
    def __init__(self, floor, roomNumber) -> None:
        self.floor = floor
        self.roomNumber = roomNumber
        self.isFree = True
        self.person = None

    def __str__(self) -> str:
        return f"{self.floor} | {self.roomNumber}"

    def __repr__(self) -> str:
        return f"{self.floor} | {self.roomNumber}"


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Hotel:
    def __init__(self) -> None:
        self.rooms = [Room(1, 100), Room(1, 101), Room(
            1, 102), Room(2, 200), Room(2, 201), Room(2, 202), Room(3, 300), Room(3, 301), Room(3, 302)]

    def show_rooms(self):
        for room in self.rooms:
            print(room, room.isFree)

    def change_room_status(self, roomNumber, person, status):
        roomToChange = next((i, el)
                            for i, el in enumerate(self.rooms) if el.roomNumber == roomNumber)[0]
        self.rooms[roomToChange].isFree = status
        if (person and status == False):
            self.rooms[roomToChange].person = person
        else:
            self.rooms[roomToChange].person = None

    def rent_room(self, person):
        freeRooms = filter(lambda room: room.isFree == True, self.rooms)
        rooms = {}
        roomsNumbers = 1
        print("Wolne pokoje")
        for room in freeRooms:
            print(f"{roomsNumbers}) Piętro {room.floor} | numer {room.roomNumber}")
            rooms[roomsNumbers] = room
            roomsNumbers += 1

        selectedRoom = input("Wybierz pokój: ")

        self.change_room_status(
            rooms[int(selectedRoom)].roomNumber, person, False)

    def show_rented_room(self, person):
        for room in filter(lambda x: x.person != None and x.person.name == person.name, self.rooms):
            print(room)

    def deregister_room(self, person):
        for room in filter(lambda x: x.person != None and x.person.name == person.name, self.rooms):
            self.change_room_status(room.roomNumber, person, True)


hotel = Hotel()
p1 = Person("Jan Kowalski")
hotel.rent_room(p1)
hotel.show_rented_room(p1)
hotel.show_rooms()
