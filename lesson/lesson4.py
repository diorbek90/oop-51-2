# пример простого декоратора

def my_decorator(func):
    def wrapper():
        print('Перед выполнением функции')
        func()
        print("После выполнение функции")

    return wrapper


@my_decorator
def hello():
    print("Привет мир!")


# greet()  # step 1


# декоратор класса
def class_decorator(cls):
    class NewClass(cls):

        def new_method(self):
            return print("Новый метод")

    return NewClass


@class_decorator
class MyClass:

    def old_method(self):
        return print("Старый метод")


# obj = MyClass()
# obj.old_method()
# obj.new_method()


def is_admin(func):
    pass


@is_admin
def ban(user_sms):
    pass


class Person:

    # Конструктор | Магический метод
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"бла бла бла"


# obj = Person('Павел', 25)
# print(obj)


class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        print(f"{self.amount}-------{other.amount}")
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"{self.amount} som"

    def __len__(self):
        return f'pass'


# m1 = Money(100)
# m2 = Money(400)
# m3 = m1 + m2
# print(m3)


class Math:

    @staticmethod
    def add(a, b):
        return a + b


# obj3 = Math()
#
# print(obj3.add(1, 2))


class Person:
    count = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_population(cls):
        return cls.count

    @classmethod
    def create_person(cls, name):
        return cls(name)


person1 = Person('Alice')
print(person1.get_population())

person2 = Person.create_person("John")
print(person2.name)
