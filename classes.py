"""Объяснение метода super в классах"""

"""Есть какой-то класс"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def to_string(self):
       return f'{self.name} {self.age}'



"""Есть еще один класс, который наследуется от предыдущего  и переопределяем to_string, init"""

class Student(Person):
    def __init__(self,name, age, facult):
        super().__init__(name, age)
        self.facult = facult

    def to_string(self):
        string_person = super().to_string()
        return f'Студент:{self.facult} {string_person}'





"""Создадим студента"""

student_misha = Student('Миша', 18, "Экономика")

print(student_misha.to_string())

