"""
Напишите класс Person, представляющий человека, имеющий следующие атрибуты:

- имя
- возраст
- зарплата

Напишите класс Employee, у которого конструктор проверяет, что возраст не меньше 18 и не больше 127 лет.
В случае, если возраст не укладывается в заданные рамки, вызвать исключение ValueError и прервать выполнение программы.
Также в конструкторе необходимо проверять уровень зарплаты, который должен быть не меньше 16242. Вызывать ValueError
исключение.

Вызванные исключения должны пояснять в чем именно произошла ошибка.
"""


class Person:
    __slots__ = ('name', 'age', 'salary')
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Employee:

    def __init__(self, name, age, salary):
        if 18 <= age <= 127 and salary >= 16242:
            super().__init__(name, age, salary)
        else:
            raise ValueError('Оплата труда не может быть меньше 16242')



# код для проверки
employee = Employee("John", 30, 5000)
# raises ValueError('Оплата труда не может быть меньше 16242')

employee = Employee("Jane", 17, 50000)
# raises ValueError('Возраст должен быть не меньше 18 и не больше 127')

employee = Employee("Kate", 175, 50000)
# raises ValueError('Возраст должен быть не меньше 18 и не больше 127')
