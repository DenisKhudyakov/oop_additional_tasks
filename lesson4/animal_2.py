"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('Я гуляю')



class Dog(Animal):

    @staticmethod
    def bark():
        return "Bark!"

    def __repr__(self):
        return self.bark()


class Cat(Animal):
    @staticmethod
    def meow():
        return "Meow!"

    def __repr__(self):
        return self.meow()



animals = [Dog("Dog1"), Dog("Dog2"), Cat("Cat1"), Dog("Dog3")]

for animal in animals:
    # Должно выводиться Bark или Meow в зависимости от того какой класс
    print(animal)
