class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
            and course in self.courses_in_progress and grade in range(1,11):
        # assert isinstance(lecturer, Lecturer)
        # assert course in lecturer.courses_attached
        # assert course in self.courses_in_progress
        # assert grade in range(1,11)
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print("Ошибка")

    def average_rate(self):
        rates_number = 0
        rates_sum = 0
        for key, value in self.grades.items():
            rates_number += len(value)
            rates_sum += sum(value)
        return(rates_sum / rates_number)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
            f'Средняя оценка за домашние задания: {self.average_rate()}\n' \
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rate() < other.average_rate()
            
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        rates_number = 0
        rates_sum = 0
        for key, value in self.grades.items():
            rates_number += len(value)
            rates_sum += sum(value)
        return(rates_sum / rates_number)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
            f'Средняя оценка за лекции: {self.average_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rate() < other.average_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
 
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

good_student = Student('Ivan', 'Ivanov', 'male')
good_student.courses_in_progress += ['Python', 'Git']
good_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
good_reviewer = Reviewer('Some', 'Buddy')
good_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

good_lecturer = Lecturer('Some', 'Buddy')
good_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(good_lecturer, 'Python', 9)

good_student.rate_lecturer(cool_lecturer, 'Python', 10)
good_student.rate_lecturer(good_lecturer, 'Python', 9)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(good_student, 'Python', 9)

good_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(good_student, 'Python', 9)

student_list = [best_student, good_student]
lecturer_list = [cool_lecturer, good_lecturer]

def get_average_student_rating(list, course):
    rates_number = 0
    rates_sum = 0
    for student in list:
        for key, value in student.grades.items():
            if key == course:
                rates_number += len(value)
                rates_sum += sum(value)
    return(rates_sum / rates_number)

def get_average_lecturer_rating(list, course):
    rates_number = 0
    rates_sum = 0
    for lecturer in list:
        for key, value in lecturer.grades.items():
            if key == course:
                rates_number += len(value)
                rates_sum += sum(value)
    return(rates_sum / rates_number)


course = 'Python'

print(f"Cредняя оценка студентов на курсе {course} :" \
    f"{get_average_student_rating(student_list, course)}")
print(f"Cредняя оценка лекторов на курсе {course} :" \
    f"{get_average_lecturer_rating(lecturer_list, course)}")

print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print(best_student > good_student)
print(cool_lecturer > good_lecturer)