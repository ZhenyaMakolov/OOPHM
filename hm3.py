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

  # def __str__(self):
    #     res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за ДЗ: ' \
    #           f'{self.middle()} \nИзучаемые курсы: {self.courses_in_progress}' \
    #           f'\nПройденные курсы: {self.finished_courses}'
    #     return res
 
class Mentor:
    def __init__(self, name, surname): # инициализация
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname, gender): # инициализация
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # def _aver_rating(self): # средний балл
    #     _sum = 0
    #     counter = 0
    #     for value in self.grades.values():
    #         for i in value:
    #             _sum += i
    #             counter += 1
    #     return round(_sum / counter, 2)

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

    def __str__(self): # строка
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade): # оценка
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)


best_lecturer = Lecturer('Ruoy', 'Eman', 'your_gender')
best_lecturer.courses_in_progress += ['Python']
 
cool_student = Student('Some', 'Buddy', 'Man')
cool_student.courses_attached += ['Python']
 
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
 
print(best_lecturer.grades)

print(Reviewer('Вася', 'Пупкин'))

print(Lecturer('Виктор', 'Кононенко', 'муж'))

# Reviewer.courses_in_progress = 'JavaScript'

# Reviewer.courses_in_progress = 'Основы программирования'

# print(Reviewer('Иван', 'Болдырев', 'муж', courses_in_progress, courses_in_progress))

print(best_lecturer)