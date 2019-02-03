class Bill():
    def __init__(self, color):
        self.color = color


class Tail():
    def __init__(self, length):
        self.length = length


class Duck():
    def __init__(self, biil, tail):
        self.bill = bill
        self.tail = tail

    def status(self):
        print('이 오리는 %s의 부리와 %dcm 길이의 꼬리를 가집니다.'
              % (self.bill.color, self.tail.length))


tail = Tail(10)
bill = Bill('주황색')
duck = Duck(bill, tail)
duck.status()
