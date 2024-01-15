from datetime import datetime
"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        if datetime.now() > datetime.strptime(str(year), '%Y'):
            self.year = year
        else:
            raise Exception('Эта машина еще не была выпущена')

# код для проверки
car = Car("Toyota", "Corolla", 2022)

car1 = Car("Toyota", "Corolla", 3000)
# raises Exception('Эта машина еще не была выпущена')
