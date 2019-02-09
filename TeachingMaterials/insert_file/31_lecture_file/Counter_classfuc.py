class Counter:
    counter_num = 0

    def __init__(self, name, count=0):
        self.name = name
        self.count = count

    @classmethod
    def print_class_num(cls):
        print("계수기 클래스 속성 값: %d" % cls.counter_num)

    def print_instance_num(self):
        print("참새 계수기 인스턴스 속성 값: %d"
              % self.counter_num)
        self.counter_num += 1


sparrow_counter = Counter("참새")
Counter.print_class_num()
# 클래스 메서드는 인스턴스에서 사용가능
sparrow_counter.print_class_num()
print("참새 계수기 속성 값-클래스 직접 접근: %d"
      % sparrow_counter.counter_num)
# 인스턴스 속성이 생성
sparrow_counter.print_instance_num()
Counter.print_class_num()
print("참새 계수기 인스턴스 속성 값: %d"
      % sparrow_counter.counter_num)
