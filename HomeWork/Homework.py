

class Heroes:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"My name is {self.name}, I have {self.hp} hp")

    def attack(self):
        print(f"I'm attacking!")


class Archer(Heroes):

    def __init__(self, arrows=5, precision=3, name="John Doe", hp=100):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        self.arrows -= 1

        if self.precision >= 1:
            print("Attack successful!")

        else:
            print("Attack failed!")

    def rest(self):
        self.arrows += 5
        print("Added 5 arrow!")

    def status(self):
        print(f"Name: {self.name}, hp: {self.hp}, count of arrows: {self.arrows}, precision: {self.precision}")


atrey = Archer(name='Atrey', hp=100, arrows=10, precision=2)
atrey.action()
atrey.attack()
atrey.rest()
atrey.status()






