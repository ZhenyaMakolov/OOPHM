class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.aver_sum}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return res

    def aver_garde(self):
        sum = 0
        count = 0

        for value in self.grades.values():
            sum += value
            count += 1
        return(sum / count, 2)

    def __lt__(self, other):
        if not isinstance (other, Student):
            print("Не является данным классом")
            return
        return self.grades < other.grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.aver_sum}'
        return res

    def aver_garde(self):
        sum = 0
        count = 0

        for value in self.grades.values():
            sum += value
            count += 1
        return(sum / count, 2)


    def __lt__(self, other):
        if not isinstance (other, Lecturer):
            print("Не является данным классом")
            return
        return self.grades < other.grades


class Reviewer (Mentor):

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res




    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




def average_grade_student(student, course):
    _sum = 0
    for student in student_all:
        if isinstance(student, Student) and course in student_grades:
            _sum.extend(student.grades[course])
        else:
            print("Error")
            return
    return f"Средняя оценка по {course}: {round(sum(_sum) / len(_sum), 2)}"


def average_grade_lector(lecturer, course):
    _sum = 0
    for lector in lecturer_all:
        if isinstance(lector, Lecturer) and course in lecturer_grades:
            _sum.extend(lecturer.grades[course])
        else:
            print("Error")
            return
    return f"Средняя оценка по {course}: {round(sum(_sum) / len(_sum), 2)}"








best_lecture = Lecturer('Ruoy', 'Eman', 'male')
best_lecture.courses_in_progress += ['Python']

cool_student = Student('Georg', 'Smit', 'male')
cool_student.courses_attached += ['Python']

cool_student.rate_hw(best_lecture, 'Python', 6)
cool_student.rate_hw(best_lecture, 'Python', 8)
cool_student.rate_hw(best_lecture, 'Python', 4)

best_lecture = Lecturer('Pol', 'Eman', 'male')
best_lecture.courses_in_progress += ['Git']

cool_student = Student ('Bob', 'Smit', 'male')
cool_student.courses_attached += ['Python']

cool_student.rate_hw(best_lecture, 'Git', 10)
cool_student.rate_hw(best_lecture, 'Git', 7)
cool_student.rate_hw(best_lecture, 'Git', 9)





best_student = Student('Bil', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer ('Arnold', 'Smit')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student = Student('Ann', 'Eman', 'female')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer ('Arnold', 'Smit')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 2)




best_lecture = Lecturer('Kate', 'Eman', 'female')
best_lecture.courses_in_progress += ['Python']


cool_student.rate_hw(best_student, 'Python', 8)
cool_student.rate_hw(best_student, 'Python', 6)
cool_student.rate_hw(best_student, 'Python', 9)

best_lecture = Lecturer('Ann', 'Eman', 'female')
best_lecture.courses_in_progress += ['Python']


cool_student.rate_hw(best_student, 'Python', 6)
cool_student.rate_hw(best_student, 'Python', 5)
cool_student.rate_hw(best_student, 'Python', 2)


student_all = [cool_student, best_student]
lecturer_all = [best_lecture]



print(best_student.grades)
print(best_lecture.grades)