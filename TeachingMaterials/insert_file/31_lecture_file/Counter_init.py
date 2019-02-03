class Counter:
    def __init__(self, name, count=0):
        self.name = name
        self.count = count

    def add(self, number=1):
        self.count += number

    def reset(self):
        self.count = 0

    def print_name(self):
        print(self.name)

    def print_count(self):
        print(self.count)


sparrow_counter = Counter("참새")
sparrow_counter.print_name()
sparrow_counter.print_count()
sparrow_counter.add()
sparrow_counter.print_count()
