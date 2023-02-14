class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, name_course):
        self.finished_courses.append(name_course)

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                total += i
                counter += 1
        if counter != 0:
            return round(total / counter, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за ДЗ: ' \
              f'{self.middle():.2} \nИзучаемые курсы: {self.courses_in_progress}' \
              f'\nПройденные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if self.middle() > other.middle():
            return f'Лучший студент - {self.name} {self.surname}'
        else:
            return f'Лучший студент - {other.name} {other.surname}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def middle(self):
        total = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                total += i
                counter += 1
        if counter != 0:
            res = round(total / counter, 2)
            return res

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nЛекции по курсу: ' \
              f'{self.courses_attached} \nСредняя оценка за лекции: {self.middle(): .2}'
        return res

    def __lt__(self, other):
        if self.middle() > other.middle():
            return f'Лучший лектор - {self.name} {self.surname}'
        else:
            return f'Лучший лектор - {other.name} {other.surname}'


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
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nПроверка домашних заданий по курсу: ' \
              f'{self.courses_attached}'
        return res


lecturer_one = Lecturer('Сергей', 'Воробьев')
lecturer_one.courses_attached += ['Python']
lecturer_two = Lecturer('Петр', 'Уткин')
lecturer_two.courses_attached += ['Git']

student_one = Student('Ксения', 'Кукушкина', 'ж')
student_one.finished_courses += ['Введение в программирование']
student_one.finished_courses += ['Основы Python']
student_one.courses_in_progress += ['Python']
student_one.courses_in_progress += ['Git']

student_two = Student('Николай', 'Гусев', 'м')
student_two.finished_courses += ['Введение в программирование']
student_two.courses_in_progress += ['Python']
student_two.courses_in_progress += ['Git']

reviewer_one = Reviewer('Ольга', 'Лебедева')
reviewer_one.courses_attached += ['Python']
reviewer_two = Reviewer('Олег', 'Синицин')
reviewer_two.courses_attached += ['Git']

print('Проверяющий:')
print(reviewer_one)
print()
print(reviewer_two)
print()

reviewer_one.rate_hw(student_one, 'Python', 9)
reviewer_one.rate_hw(student_one, 'Python', 8)
reviewer_one.rate_hw(student_one, 'Python', 10)

reviewer_two.rate_hw(student_one, 'Git', 8)
reviewer_two.rate_hw(student_one, 'Git', 9)
reviewer_two.rate_hw(student_one, 'Git', 9)

student_one.rate_hw(lecturer_one, 'Python', 10)
student_one.rate_hw(lecturer_one, 'Python', 9)
student_one.rate_hw(lecturer_one, 'Python', 10)

student_two.rate_hw(lecturer_one, 'Python', 9)
student_two.rate_hw(lecturer_one, 'Python', 10)
student_two.rate_hw(lecturer_one, 'Python', 9)

reviewer_one.rate_hw(student_two, 'Python', 8)
reviewer_one.rate_hw(student_two, 'Python', 8)
reviewer_one.rate_hw(student_two, 'Python', 9)

reviewer_two.rate_hw(student_two, 'Git', 7)
reviewer_two.rate_hw(student_two, 'Git', 5)
reviewer_two.rate_hw(student_two, 'Git', 9)

student_one.rate_hw(lecturer_two, 'Git', 10)
student_one.rate_hw(lecturer_two, 'Git', 9)
student_one.rate_hw(lecturer_two, 'Git', 8)

student_two.rate_hw(lecturer_two, 'Git', 9)
student_two.rate_hw(lecturer_two, 'Git', 10)
student_two.rate_hw(lecturer_two, 'Git', 7)

print('Лекторы:')
print(lecturer_one)
print()
print(lecturer_two)
print()
print('Студенты:')
print(student_one)
print()
print(student_two)
print()
print(lecturer_one.__lt__(lecturer_two))
print()
print(student_one.__lt__(student_two))
print()

students_list = [student_one, student_two]
lecturer_list = [lecturer_one, lecturer_two]


def grades_students(students_list, course):
    overall_student_rating = 0
    students = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            students += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{overall_student_rating / students:.2}'


def grades_lecturers(lecturer_list, course):
    overall_lectors_rating = 0
    lectors = 0
    for listener in lecturer_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for rates in listener.grades[course]:
                average_student_score += rates
            overall_lectors_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_lectors_rating
            lectors += 1
    if overall_lectors_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{overall_lectors_rating / lectors:.2}'


print(f'Средняя оценка студентов по курсу "Git": {grades_students(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')