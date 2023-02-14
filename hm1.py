class Student:
    def __init__(self, name, surname, gender): # инициализация
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] # завершенные курсы
        self.courses_in_progress = [] # курсы в прогрессе
        self.grades = {} # оценки
 
    def add_courses(self, course_name): # добавить курсы
        self.finished_courses.append(course_name)   
 
     
class Mentor:
    def __init__(self, name, surname): # инициализация
        self.name = name
        self.surname = surname
        self.courses_attached = [] # подключенные курсы
        
    def rate_hw(self, student, course, grade): # оценка
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    pass
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)