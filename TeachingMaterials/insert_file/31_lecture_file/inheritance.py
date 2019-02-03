class Parent:
    def __init__(self):
        print("Parent 초기화")
        self.attribute = "test"

    def parent_method(self):
        print("속성값: %s" % self.attribute)


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child 초기화")


child = Child()
child.parent_method()
