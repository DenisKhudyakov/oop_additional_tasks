"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:

    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade

    def avg_rate(self):
        return sum(self.grade) / len(self.grade) if self.grade else 0.0


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate() # 4.75
print(student.avg_rate())

student = Student('Ivan', 'Python', [])
student.avg_rate() # 0.0
print(student.avg_rate())
