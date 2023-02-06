class Student:
    def __init__(self, name, surname, gender): # инициализация
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
 
    def add_courses(self, course_name): # добавить курсы
        self.finished_courses.append(course_name)  

    def rate_hw(self, lecturer, course, grade): # оценка
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self, name , surname): # строка
        res = f'Имя: {name} \nФамилия: {surname} \nСредняя оценка за лекции: {self.grades} \nКурсы в процессе изучения:{self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return res

student_list = [best_student, some_student]

    def average_rat_stud(students, course): # средняя оценка
        _sum = []
        for student in student_list:
            if isinstance(student, Student) and course in student.grades:
                _sum.extend(student.grades[course])
            else:
                print('Error.')
                return
        return f'Средняя оценка студентов по {course}: {round(sum(_sum) / len(_sum), 2)}'

print(average_rat_stud(student_list, 'Python'))

    def __lt__(self, other):

class Mentor:
    def __init__(self, name, surname): # инициализация
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname): # инициализация
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def _aver_rating(self): # средний балл
        _sum = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                _sum += i
                counter += 1
            return round(_sum / counter, 2)

    def __str__(self): # строка
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._aver_rating()}'
        return res

lecturer_list = [best_lecturer, some_lecturer]

    def __lt__(self, other): # 
        if not isinstance(other, Lecturer):
            print('Не является экземляром класса Lecturer.')
            return
        return self._aver_rating() < other._aver_rating

    def average_rat_stud(lecturers, course): #
        _sum = []
        for lecturer in lecturer_list:
            if isinstance(lecturer, Lecturers) and course in lecturer.grades:
                _sum.extend(lecturer.grades[course])
            else:
                print('Error.')
                return
        return f'Средняя оценка студентов по {course}: {round(sum(_sum) / len(_sum), 2)}'

print(average_rat_stud(lecturer_list, 'Python'))

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade): # оценка
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self, name , surname): # строка
        res = f'Имя: {name} \nФамилия: {surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)


best_lecturer = Lecturer('Ruoy', 'Eman', 'your_gender')
best_lecturer.courses_in_progress += ['Python']
 
cool_student = Student('Some', 'Buddy', 'Man')
cool_student.courses_attached += ['Python']
 
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
 
print(best_lecturer.grades)

print(best_lecturer.__lt__(some_lecturer))
print(best_student.__lt__(some_student))

def avg_grade_curs(students, course):
    rates = []
    for student in students:
        if student[course]:
            rates.extend(student[course])
    return round(sum(rates) / len(rates), 2)


print(avg_grade_curs(student_list, course='Git'))