

# class def

class Person:

    # Это Функция Конструктор
    def __init__(self, name, age):
        # атрибуты класса
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi I'm {self.name}")


# ardager = Person("Ardager", 25)
#
# ardager.introduce()
#
# print(type(ardager))
# print(type(123))
# print(type('Hello'))

class Hero:

    def __init__(self, name, hp, lvl):

        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        print(f"{self.name} делает базовое действие")

# neofume = Hero('Naofume', 100, 3)

# class -- CamelCase
# перемнные, методы, функции -- snek_case

class Shiledhero(Hero):
    pass

naofume = Shiledhero('Nafume', 100, 3)