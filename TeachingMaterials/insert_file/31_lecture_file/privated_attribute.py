class Dog():
    def __init__(self):
        self.__value = "happy"

    def get(self):
        return self.__value


class Beagle(Dog):
    def __init__(self):
        super().__init__()
        self.__value = 5

    def get_value(self):
        return self.__value


my_dog = Beagle()
my_dog.__value = 10
print("my_dog value의 값", my_dog.get_value())
print(my_dog.__dict__)
my_dog._Dog__value = "revise"
print(my_dog.get())
