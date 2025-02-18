# # множественное наследование
#
#
# # горизантальное наследование
# class Flyable:
#
#     def fly(self):
#         return 'Летет'
#
#
# class Swimmable:
#
#     def swim(self):
#         return "Плавает"
#
#
# class Duck(Flyable, Swimmable):
#
#     def make_sound(self):
#         return "Кря-Кря!!"
#
#
# donald_duck = Duck()
# print(donald_duck.fly())
# print(donald_duck.swim())


# ромбовидное наследование

# class Animal:
#
#     def make_sound(self):
#         return 'издает звук'
#
#
# class Flyable(Animal):
#
#     def action(self):
#         return 'Летет'
#
#
# class Swimmable(Animal):
#
#     def action(self):
#         return "плавает"
#
#
# class Duck(Flyable, Swimmable):
#
#     def make_sound(self):
#         return "Кря-Кря!!"
#
#
# donald_duck = Duck()
# print(donald_duck.action())
# print(Duck.mro())


import sqlite3

connect = sqlite3.connect('User.db')

cursor = connect.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
        name TEXT NOT NULL, 
        age INTEGER, 
        hobby TEXT NOT NULL
    )
    '''
)

connect.commit()


def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


# add_user("Ardager", 33, 'спать')
# add_user("Вася", 45, 'бегать')
# add_user('Олег', 11, 'ничего')


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)
    print('Список всех пользователей')
    for i in users:
        print(f'NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}')

    users = cursor.fetchall()


get_all_users()
