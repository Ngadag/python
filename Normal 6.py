class School:
    def __init__(self, school_name, address, list_teachers, list_students):
        self.school_name = school_name
        self.address = address
        self.list_teachers = list_teachers
        self.list_students = list_students
    def get_classes(self):
        classes = set([student.get_class_room for student in self.list_students])
        return list(sorted(classes))

    def get_students_inclass(self, class_room):
        return [student.get_full_name for student in self.list_students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_full_name for teacher in self.list_teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self.list_students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_full_name for teachers in
                            self.list_teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_subjects for teachers in
                           self._list_teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                    }

    def __str__(self):
        return '[%s, %s]' %(self.school_name, self.address)


class Class(School):
    def __init__(self, class_room, list_subjects):
        School. __init__(self, school_name, address, list_teachers, list_students)
        self.class_room = class_room
        self.list_subjects = list_subjects

    def get_list_subjects(self):
        return self.class_room + "Subjects are: " + self.list_subjects


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


    def get_full_name(self):
        return '{0} {1} '.format(self._last_name,
                                    self._first_name)

class Student(Person):
    def __init__(self, last_name, first_name, class_room, subjects, mother, father):
        super().__init__(self, last_name, first_name)
        self.class_room = class_room
        self.subjects = subjects
        self.parents = {
            'mother' : mother,
            'father' : father
        }

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.parents

class Teacher(Person):
    def __str__(self, last_name, first_name, subjects, list_classes):
        super().__init__(self, last_name, first_name)
        self.subjects = subjects
        self.list_classes = list_classes

    def get_subjects(self):
        return self.subjects

    def get_classes(self):
        return self.list_classes

teacher1 = Teacher('Ivanov', 'Ivan', ['Maths', 'Geometry', 'Algebra'], ['4A', '4B', '5A', '5B'])
list_teachers = [
    Teacher('Ivanov', 'Ivan', ['Maths', 'Geometry', 'Algebra'], ['4A', '4B', '5A', '5B']),
    Teacher('Petrov', 'Petr', ['Physics', 'Astronomy'], ['9A', '9B', '10A', '10B']),
    Teacher('Sidorov', 'Sidor', ['Literature', 'Russian language'], ['4A', '5A', '10B'])
]


list_students = [
    Student('Kuznetsov', 'Sergey', '5A', ['Maths', 'Physics', 'Literature'], 'Kuznethsova Galina', 'Kuznetsov Mikhail'),
    Student('Smirnov', 'Anton', '4A', ['Maths', 'Physics', 'Literature', 'Russian language'], 'Smirnova Olga', 'Smirnov Vasiliy'),
    Student('Ostromova', 'Elena', '3A', ['Nature', 'Literature'], 'Ostromova Irina', 'Ostromov Alexander')]

school_name = School('5-Gimansium', 'Moscow', list_teachers, list_students)
