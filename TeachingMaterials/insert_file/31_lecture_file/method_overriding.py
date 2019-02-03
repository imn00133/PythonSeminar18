class Character:
    def __init__(self):
        self.inteligence = 10
        self.strength = 10

    def attack(self):
        print("공격력: %f" % (self.strength*0.5))


class Warrior(Character):
    def __init__(self):
        super().__init__()
        self.additional_strength = 20

    def attack(self):
        super().attack()
        print("추가 공격력: %f" % (self.additional_strength*0.5))


warrior = Warrior()
warrior.attack()
