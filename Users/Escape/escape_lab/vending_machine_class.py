class vending_machine(object):
    def __init__(self):
        self.__productnames = list()
        self.__productprices = list()
        self.__productstock = list()
        self.__money = 0
        self.__queue = list()

    # 돈이 얼마요
    @property
    def money(self):
        return self.__money

    # 돈을 넣는 것
    def money_in(self, value):
        if value > 0:
            self.__money += value
        else:
            raise ValueError

    # 돈을 빼는 것
    # 실패 시 에러 발생
    def money_out(self, value):
        if 0 <= value <= self.__money:
            self.__money -= value
        else:
            raise ValueError

    # 물품을 살 수 있는지 여부 구하기
    def purchasable(self, index, amount=1):
        return self.__money > self.__productprices[index] * amount and \
               self.__productstock[index] >= amount

    def add(self, name, price, stock):
        self.__productnames.append(name)
        self.__productprices.append(price)
        self.__productstock.append(stock)

    # 편의를 위해 리필 수량이 음수인 경우에도 작동 가능
    def refill(self, index, amount):
        if int(amount) == amount and self.__productstock[index] + amount >= 0:
            self.__productstock[index] += amount
        else:
            raise ValueError

    @property
    def productcount(self):
        return len(self.__productnames)

    def purchase(self, index, amount=1):
        if int(amount) == amount and amount >= 0:  # \
            # and self.purchasable(index, amount):
            for purchase in range(0, amount):
                if self.__money <= 0 or self.__productstock[index] <= 0:
                    break
                else:
                    self.__productstock[index] -= 1
                    self.__money -= self.__productprices[index]
                    self.__queue.append(index)

    @property
    def queue(self):
        return self.__queue


a = vending_machine()
a.add('우웩', 200, 100)
a.add('우웨엑', 300, 3)
a.money_in(10000)
a.purchase(0, 3)
print(a.queue)
a.purchase(1, 5)
print(a.queue)
