import random


class Teacher:
    def __init__(self, firstName, lastName, title) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.title = title

    def check_exam(self, ratio):
        if ratio >= 3:
            return "Przedmiot Zaliczonu"
        else:
            return "Przedmiot do poprawy"


class Subject:
    def __init__(self, name, teacher) -> None:
        self.rating = "Nie zaliczany"
        self.name = name
        self.teacher = Teacher(
            teacher.firstName, teacher.lastName, teacher.title)

    def exam(self):
        self.rating = self.teacher.check_exam(random.randint(1, 5))


class Student:
    def __init__(self, name, index) -> None:
        self.subjects = []
        self.name = name
        self.index = index

    def add_subject(self, name, teacher):
        self.subjects.append(Subject(name, teacher))

    def check_subjects_pass(self):
        for subject in self.subjects:
            print(subject.name + ": " + subject.rating)

    def write_exam(self, subjectName):
        filtredSubject = next(
            (item for item in self.subjects if item.name == subjectName), None)

        if filtredSubject != None:
            filtredSubject.exam()


student = Student("Grzegorz", 32143)

student.add_subject("Matematyka", Teacher("Jan", "Kowalski", "Prof"))
student.add_subject("Fizyka", Teacher("Tomasz", "Bąk", "Prof"))

student.write_exam("Matematyka")
student.write_exam("Fizyka")

student.check_subjects_pass()
