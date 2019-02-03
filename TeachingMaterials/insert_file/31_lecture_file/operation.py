class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.attack = 10
        self.defence = 5

    def __eq__(self, other):
        return self.name == other.name

    def __sub__(self, other):
        self.hp = self.hp + self.defence - self.attack
        print("현재 %s의 hp는 %d입니다." % (self.name, self.hp))


jaehyeong = Character("재형")
youngchun = Character("영천")
jaehyeong2 = Character("재형")

print("재형과 영천은 같은가?")
print(jaehyeong == youngchun)
print("재형2는 재형의 부계정인가?")
print(jaehyeong == jaehyeong2)

jaehyeong - youngchun
