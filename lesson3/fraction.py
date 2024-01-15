"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __repr__(self):
        return f'Fraction({self.num1}, {self.num2})'

    def __str__(self):
        return f'{self.num1}/{self.num2}'

    def __add__(self, other):
        if self.num2 % other.num2 == 0:
            new_num = self.num2 / other.num2 * other.num1
            return f'{new_num + self.num1}/{self.num2}'
        elif other.num2 % self.num2 == 0:
            new_num = other.num2 / self.num2 * self.num1
            return f'{other.num1 + int(new_num)}/{other.num2}'


# код для проверки
fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
