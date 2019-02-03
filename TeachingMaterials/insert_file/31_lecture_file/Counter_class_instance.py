class Counter:
    count_num = 0

    def __init__(self, name, count=0):
        self.name = name
        self.count = count

    @classmethod
    def print_class_num(cls):
        print(cls.count_num)

    def print_instance_num(self):
        print(self.count_num)


Counter.print_class_num()
Counter.count_num = 2
Counter.print_class_num()

sparrow_counter = Counter("참새")
sparrow_counter.count_num = 5
print("인스턴스 값: %d" % sparrow_counter.count_num)
print("클래스 값: %d" % Counter.count_num)
sparrow_counter.print_instance_num()

Counter.print_instance_num()
