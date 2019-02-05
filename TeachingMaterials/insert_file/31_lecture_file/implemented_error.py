class Dog():
    def bark(self):
        raise NotImplementedError("bark메서드가 구현되지 않음")


class Beagle(Dog):
    pass


my_dog = Beagle()
my_dog.bark()
