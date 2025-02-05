class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.hp}")

    def is_adult(self):

        if self.lvl >= 10:
            return True
        else:
            return False


main_hero = Hero('Arthas', 99, 1200)
main_hero.introduce()
print(main_hero.is_adult())

hero_light = Hero('Alukard', 9, 100)
hero_light.introduce()
print(hero_light.is_adult())



