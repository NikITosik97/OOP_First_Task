class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        if course_name not in self.finished_courses:
            self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_l:
                lecturer.grades_l[course] += [grade]
            else:
                lecturer.grades_l[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        for lst in self.grades.values():
            count = 0
            for digit in lst:
                count += digit
            res = count / len(lst)
        return res

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка при сравнение'
        elif self.average_rating() > other.average_rating():
            return f'Средний балл студента: {self.name}, больше среднего балла студента: {other.name}'
        elif self.average_rating() < other.average_rating():
            return f'Средний балл студента: {self.name}, меньше среднего балла студента: {other.name}'
        else:
            return f'Средний балл студента: {self.name}, равен среднему баллу студента: {other.name}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_l = {}

    def average_rating(self):
        for lst in self.grades_l.values():
            count = 0
            for digit in lst:
                count += digit
            res = count / len(lst)
            return res

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            return 'Ошибка при сравнение'
        elif self.average_rating() > other.average_rating():
            return f'Средний балл лектора: {self.name}, больше среднего балла лектора: {other.name}'
        elif self.average_rating() < other.average_rating():
            return f'Средний балл лектора: {self.name}, меньше среднего балла лектора: {other.name}'
        else:
            return f'Средний балл лектора: {self.name}, равен среднему баллу лектора: {other.name}'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student('Альфредо', 'Добрый', 'Man')
student1.finished_courses.append('Введение в программирование')
student1.courses_in_progress.append('Python')
student1.courses_in_progress.append('Git')

student2 = Student('Эмма', 'Оушин', 'Girl')
student2.finished_courses.append('Введение в программирование')
student2.courses_in_progress.append('Git')
student2.courses_in_progress.append('Python')

lecturer1 = Lecturer('Алиша', 'Бьют')
lecturer1.courses_attached.append('Python')

lecturer2 = Lecturer('Нейтан', 'Бабушкин')
lecturer2.courses_attached.append('Git')
lecturer2.courses_attached.append('Python')

reviewer1 = Reviewer('Кристина', 'Белочкина')
reviewer1.courses_attached.append('Python')

reviewer2 = Reviewer('Ольга', 'Ждунова')
reviewer2.courses_attached.append('Git')

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'Git', 10)

student1.rate_hw(lecturer1, 'Python', 9)
student1.rate_hw(lecturer1, 'Git', 7)
student1.rate_hw(lecturer2, 'Python', 10)
student1.rate_hw(lecturer2, 'Git', 4)

student2.rate_hw(lecturer1, 'Python', 5)
student2.rate_hw(lecturer1, 'Git', 6)
student2.rate_hw(lecturer2, 'Python', 4)
student2.rate_hw(lecturer2, 'Git', 7)


def counting_student(lst_stud, course):
    c = []
    x = 0
    for stud in lst_stud:
        if course in stud.grades:
            for i in stud.grades['Python']:
                c.append(i)
                x += i
    return f'Средний балл всех студентов по курсу \'Python\': {x / len(c)}'


def counting_lecturer(lst_lect, course):
    c = []
    x = 0
    for lect in lst_lect:
        if course in lect.grades_l:
            for i in lect.grades_l['Python']:
                c.append(i)
                x += i
    return f'Средний балл всех лекторов по курсу \'Python\': {x / len(c)}'


lst_student = [student1, student2]
lst_lecturer = [lecturer1, lecturer2]
lst_course = 'Python'


print(reviewer1)
print('-' * 90)
print(lecturer1)
print('-' * 90)
print(student1)
print('-' * 90)
print(lecturer1 < lecturer2)
print('-' * 90)
print(student1 < student2)
print('-' * 90)
print(counting_student(lst_student, lst_course))
print('-' * 90)
print(counting_lecturer(lst_lecturer, lst_course))
