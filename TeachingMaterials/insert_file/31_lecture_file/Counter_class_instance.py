class Counter:
    counter_num = 0

    def __init__(self, name, count=0):
        self.name = name
        self.count = count

    @classmethod
    def print_class_num(cls):
        print("클래스 값: %d" % cls.counter_num)

    def print_instance_num(self):
        print("인스턴스 값: %d" % self.counter_num)


# 직접 클래스 속성 접근 변경
Counter.print_class_num()
Counter.counter_num = 2
Counter.print_class_num()

# 인스턴스 변수 할당
sparrow_counter = Counter("참새")
sparrow_counter.counter_num = 5
print("인스턴스 값: %d" % sparrow_counter.counter_num)
print("클래스 값: %d" % Counter.counter_num)
sparrow_counter.print_instance_num()

# 클래스에서 인스턴스 메소드 실행
Counter.print_instance_num()
