from typing import Dict, Any

students_list = []
lecturer_list = []


def medium_grades(some_list, courses):
    if type(some_list) == type(students_list) and type(courses) == str:
        medium_grade = 0
        for student in students_list:
            for key in student.grades.keys():
                if courses == key:
                    medium_grade += sum(student.grades[courses]) / len(student.grades[courses])
    else:
        return 'ОШИБКА ВВОДА'
    medium_grades_all = medium_grade / len(students_list)
    return medium_grades_all if medium_grade > 0 else "Курс не найден"


def medium_grades_lecturer(some_list, courses):
    medium_grade = 0
    if type(some_list) == type(lecturer_list) and type(courses) == str:
        for lecturer in lecturer_list:
            for key in lecturer.grades.keys():
                if courses == key:
                    medium_grade += sum(lecturer.grades[courses]) / len(lecturer.grades[courses])
    else:
        return 'ОШИБКА ВВОДА'
    medium_grades_all = medium_grade / len(lecturer_list)
    return medium_grades_all if medium_grade > 0 else "Курс не найден"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __get_average(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        average = sum(all_grades) / len(all_grades)
        return average

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:' \
               f' {self.__get_average()}\nКурсы в процессе изучения:  {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        if not isinstance(other, (float, int, Student)):
            raise TypeError('Операнд должен иметь тип int, float или Sudent')
        sc = other if isinstance(other, int) else other.__get_average()
        return self.__get_average() == sc

    def __lt__(self, other):
        if not isinstance(other, (float, int, Student)):
            raise TypeError('Операнд должен иметь тип int, float или Sudent')
        sc = other if isinstance(other, int) else other.__get_average()
        return self.__get_average() < sc

    def __le__(self, other):
        if not isinstance(other, (float, int, Student)):
            raise TypeError('Операнд должен иметь тип int, float или Sudent')
        sc = other if isinstance(other, int) else other.__get_average()
        return self.__get_average() <= sc


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.grades = {}
        lecturer_list.append(self)
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__get_average()}"

    def __get_average(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        average = sum(all_grades) / len(all_grades)
        return average

    def __eq__(self, other):
        if not isinstance(other, (float, int, Lecturer)):
            raise TypeError('Операнд должен иметь тип int, float или Lecturer')
        sc = other if isinstance(other, int) else other.__get_average()
        return self.__get_average() == sc

    def __lt__(self, other):
        if not isinstance(other, (float, int, Lecturer)):
            raise TypeError('Операнд должен иметь тип int, float или Lecturer')
        sc = other if isinstance(other, int) else other.__get_average()
        return self.__get_average() < sc

    def __le__(self, other):
        if not isinstance(other, (float, int, Lecturer)):
            raise TypeError('Операнд должен иметь тип int, float или Lecturer')
        sc = other if isinstance(other, int) else other.__get_average()
        return self.__get_average() <= sc


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['JS']
bad_student = Student('Vasya', 'Pupkin', 'M')
bad_student.courses_in_progress += ['Python']
bad_student.finished_courses += ['C']
cool_reviewer = Reviewer('Some', 'Buddy')
bad_reviewer = Reviewer('Petya', 'Dudkin')

cool_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(bad_student, 'Python', 5)
bad_reviewer.rate_hw(best_student, 'Python', 10)
bad_reviewer.rate_hw(bad_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 9)
bad_reviewer.rate_hw(bad_student, 'Python', 10)

main_lecturer = Lecturer('Lisa', 'Liza')
main_lecturer.courses_attached += ['Python']

best_lecturer = Lecturer('Anna', 'Petrova')
best_lecturer.courses_attached += ['Python']

bad_student.rate_lec(main_lecturer, 'Python', 5)
best_student.rate_lec(main_lecturer, 'Python', 8)

bad_student.rate_lec(best_lecturer, 'Python', 6)
best_student.rate_lec(best_lecturer, 'Python', 8)

print(best_student.grades)
print(cool_reviewer)
print(best_lecturer)
print(best_student)
print(bad_student)
print(best_student == bad_student)
print(best_student >= bad_student)
print(best_student < bad_student)
print(main_lecturer != best_lecturer)
print(main_lecturer <= best_lecturer)
print(main_lecturer < best_lecturer)
print(medium_grades(students_list, 'Python'))
print(medium_grades(students_list, 'sss'))
print(medium_grades_lecturer(lecturer_list, 'Python'))
print(medium_grades_lecturer("students_list", 'Python'))
