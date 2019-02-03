class Counter:
    def set_count(self, count=0):
        self.count = count

    def set_name(self, name):
        self.name = name

    def add(self, number=1):
        self.count += number

    def reset(self):
        self.count = 0

    def print_name(self):
        print(self.name)

    def print_count(self):
        print(self.count)


sparrow_counter = Counter()
# sparrow_counter.set_count()
# sparrow_counter.set_name("참새")
sparrow_counter.add(4)
sparrow_counter.print_name()
sparrow_counter.print_count()
