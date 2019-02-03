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
        self.count_num += 1


print("계수기 클래스 속성 값: %d" % Counter.count_num)
sparrow_counter = Counter("참새")
# 클래스 메서드는 인스턴스에서 사용가능
sparrow_counter.print_class_num()
sparrow_counter.print_instance_num()
print("계수기 클래스 속성 값: %d" % Counter.count_num)
print("참새 계수기 인스턴스 값: %d" % sparrow_counter.count_num)
sparrow_counter.print_instance_num()
print("참새 계수기 인스턴스 값: %d" % sparrow_counter.count_num)
