class Counter:
    counter_count = 0

    def __init__(self, name, count=0):
        self.name = name
        self.count = count
        self.add_counter()

    def __del__(self):
        self.del_counter()

    @classmethod
    def add_counter(cls):
        cls.counter_count += 1

    @classmethod
    def del_counter(cls):
        cls.counter_count -= 1

    @classmethod
    def print_counter_count(cls):
        print("현재 계수기 개수: %d" % cls.counter_count)

    def add(self, number=1):
        self.count += number

    def reset(self):
        self.count = 0

    def print_name(self):
        print(self.name)

    def print_count(self):
        print(self.count)


sparrow_counter = Counter("참새")
sparrow_counter.print_counter_count()
pigeon_counter = Counter("비둘기")
pigeon_counter.print_counter_count()
del(pigeon_counter)
Counter.print_counter_count()
