import datetime
"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""


class Timer:
    def __enter__(self):
        self.start = datetime.datetime.now()
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        self.delta = self.start - self.end

    @property
    def elapsed_time(self):
        return self.delta

with Timer() as timer:
    print(timer)

# код для проверки 
print("Execution time:", timer.elapsed_time)
