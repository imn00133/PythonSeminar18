class Person():
    def __init__(self, new_name):
        self._name = new_name

    def get_name(self):
        print("획득자 실행")
        return self._name

    def set_name(self, new_name):
        print("설정자 실행")
        self._name = new_name

    name = property(get_name, set_name)


who = Person("재형")
print(who.name)
who.name = '영천'
print(who.name)
