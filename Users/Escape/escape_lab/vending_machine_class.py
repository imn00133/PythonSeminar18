class VendingMachine:
    INDEX_START = 1

    def __init__(self):
        self._product = list()
        self._money = 0

    # 돈이 얼마요(읽기 전용)
    @property
    def money(self):
        return self._money

    # 돈을 넣는 것
    def money_in(self, value):
        if value >= 0:
            self._money += value
        else:
            raise ValueError

    # 돈을 빼는 것
    # 매개 변수 없이 쓰면 전부 반환
    # 실패 시 에러 발생
    def money_out(self, value=None):
        if value is None:
            self._money = 0
        elif 0 <= value <= self._money:
            self._money -= value
        else:
            raise ValueError

    def add(self, name, price, amount=0):
        self._product.append(Product(name, price, amount))

    def delete(self, index, alert=False):
        if alert:
            print('%s을(를) 제거합니다.' %
                  self._product[index - self.INDEX_START].name)
        del(self._product[index - self.INDEX_START])

    @property
    def productcount(self):
        return len(self._product)

    def product(self, index=None):
        if index is None:
            return self._product
        else:
            return self._product[index - self.INDEX_START]

    def purchase(self, index, amount=1):
        if int(amount) == amount and amount >= 0:  # \
            # and self.purchasable(index, amount):
            success = 0
            choice = self._product[index - self.INDEX_START]
            for purchase in range(0, amount):
                if self._money <= 0 or choice.amount <= 0:
                    break
                else:
                    choice.amount -= 1
                    success += 1
                    self._money -= choice.price
            return success


class Product:
    def __init__(self, name, price, amount=0):
        self._name = name
        self._price = price
        self._amount = amount

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def amount(self):
        return self._amount

    # 유효성 검사 부분 집어넣기
    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self.price = price

    @amount.setter
    def amount(self, amount):
        self._amount = amount


def load_product(file_name='product.met'):
    result = VendingMachine()
    with open(file_name, mode='r', encoding='UTF-8') as f:
        for line in f.readlines():
            if line[0] == '(' and line[-2] == ')':
                product = line[1:len(line) - 2].split(',')
                for i, detail in enumerate(product):
                    product[i] = detail.strip()
                product[1], product[2] = int(product[1]), int(product[2])
                result.add(product[0], product[1], product[2])
    return result


def save_product(vending_machine, file_name='product.met'):
    with open(file_name, mode='w', encoding='UTF-8') as f:
        # p = product
        for p in vending_machine.product():
            f.write(
                '(%s)\n' % ', '.join([p.name, str(p.price), str(p.amount)])
            )


def customer_mode():
    # 돈 넣고
    money_in()
    while True:
        task = customer_task().lower()
        # task 반환값
        # 'admin': 관리자 모드 진입
        # 'in'   : 돈 넣기
        # 'out'  : 거스름돈
        # 'exit' : 종료
        # (int)  : 해당 번호의 물품 구매

        if task.isnumeric():
            purchase(int(task))
        else:
            if task == 'admin':
                admin_mode()
            elif task == 'in':
                money_in()
            elif task == 'out':
                money_out()
            elif task == 'exit':
                money_out()
                exit_program()


def admin_mode():
    while True:
        task = admin_task()
        if task == 'add':
            add_product()
        if task == 'modify':
            modify_product()
        if task == 'delete':
            delete_product()
        if task == 'info':
            show_product(True)
        if task == 'refill':
            refill_product()
        if task == 'exit':
            print('관리자 모드를 종료합니다.')
            break


def exit_program():
    print('자판기 이용을 종료합니다.')
    exit()


def money_in():
    money = input('돈을 넣으세요: ')
    # 돈 대신 이상한 거 넣으면 걸러내는 부분
    while True:
        try:
            if int(money) < 0:
                raise ValueError
        except ValueError:
            # 실패할 경우 다시 입력받습니다.
            money = input('돈을 제대로 넣으세요: ')
        else:
            machine.money_in(int(money))
            break


def money_out():
    save_product(machine)
    if machine.money > 0:
        print('%d원이 반환됩니다.' % machine.money)
        machine.money_out()
    else:
        print('잔액이 없어 돈이 반환되지 않습니다.')


def show_product(show_amount=False):
    for cnt, p in enumerate(machine.product(), start=1):
        if show_amount:
            print('%d. %s(%d원) 재고량: %d' % (cnt, p.name, p.price, p.amount))
        else:
            print('%d. %s(%d원)' % (cnt, p.name, p.price))


def customer_task():
    # 호갱 모드의 작업 수행
    while True:
        show_product()
        cnt = machine.productcount

        print('%d. 돈 넣기' % (cnt + 1))
        print('%d. 거스름돈' % (cnt + 2))
        print('%d. 종료' % (cnt + 3))

        # 하게 될 동작을 선택받습니다.
        try:
            product = input('잔액: %d원\n뽑을 물품을 선택해주세요: ' % machine.money)
            if not product.isnumeric():
                if product.lower() == 'admin':
                    return 'admin'
                else:
                    raise ValueError
            else:
                product = int(product)
                if product > cnt + 3 or product < 0:
                    raise ValueError
                # 돈을 넣으려고 한 경우
                elif product == cnt + 1:
                    return 'in'
                # 거스름돈을 선택한 경우
                elif product == cnt + 2:
                    return 'out'
                # 종료를 시도한 경우
                elif product == cnt + 3:
                    return 'exit'
                # 물품을 선택한 경우
                else:
                    return str(product)
        except UnicodeDecodeError:
            print('다시 입력해주세요.')
        except ValueError:
            print('물품 번호를 잘못 입력하셨습니다.')


def admin_task():
    while True:
        action = input('''관리자 모드
1. 물품 추가
2. 물품 정보 변경
3. 물품 삭제
4. 물품 정보 확인
5. 재고 추가
6. 종료
진행할 작업을 선택하세요: ''')
        if action == '1':
            return 'add'
        elif action == '2':
            return 'modify'
        elif action == '3':
            return 'delete'
        elif action == '4':
            return 'info'
        elif action == '5':
            return 'refill'
        elif action == '6':
            return 'exit'
        else:
            print('잘못 입력하셨습니다.')
            continue
        break


def add_product():
    while True:
        print("새 물품을 추가합니다.")
        name = input("이름을 입력해주세요: ")
        price = input("가격을 입력해주세요: ")
        amount = input("수량을 입력해주세요: ")

        try:
            machine.add(name, int(price), int(amount))
            break
        except ValueError:
            print("입력값이 잘멧되었습니다.")    # 못
            continue


def modify_product():
    while True:
        while True:
            print("물품의 정보를 수정합니다.")
            show_product()
            try:
                index = input('정보를 수정할 물품을 선택해주세요: ')
                if not index.isnumeric():
                    raise ValueError
                else:
                    index = int(index)
                    if not 0 <= index - VendingMachine.INDEX_START \
                             <= machine.productcount:
                        raise ValueError
            except ValueError:
                print('입력값이 잘멧되었습니다.')
                continue
            else:
                break

        name = input("이름을 입력해주세요: ")
        price = input("가격을 입력해주세요: ")
        try:
            if name.strip() != '':
                machine.product(index).name = name.strip()
            if price.strip() != '':
                machine.product(index).price = int(price)
            break
        except ValueError:
            print("입력값이 잘멧되었습니다.")    # 못
            continue


def delete_product():
    while True:
        print("물품을 삭제합니다.")
        show_product()

        index = input('삭제할 물품을 선택해주세요: ')
        try:
            machine.delete(int(index), alert=True)
        except ValueError:
            print('입력값이 잘멧되었습니다.')
            continue
        except IndexError:
            print('입력값이 잘멧되었습니다.')
            continue
        else:
            break


def refill_product():
    while True:
        print("물품의 재고를 추가합니다.")
        show_product(True)
        try:
            index = input('물품을 선택해주세요: ')
            machine.product(int(index))
        except ValueError:
            print('입력값이 잘멧되었습니다.')
            continue
        except IndexError:
            print('입력값이 잘멧되었습니다.')
            continue
        else:
            break

    while True:
        amount = input("추가할 수량을 입력해주세요: ")
        try:
            machine.product(int(index)).amount += int(amount)
            break
        except ValueError:
            print("입력값이 잘멧되었습니다.")    # 못
            continue


def purchase(index):
    # 리스트는 0번부터 시작하는데 물품번호는 1번부터 시작이므로 1을 빼줍니다.
    # 돈이 충분하면 물품을 내보냅니다.
    product = machine.product(index)
    if machine.money < product.price:
        print('돈이 부족하여 구매할 수 없습니다.')
    elif product.amount <= 0:
        print('고르신 물품의 재고가 부족하여 구매가 불가능합니다.')
    else:
        machine.purchase(index)
        print('%s을(를) 구매하셨습니다.' % product.name)
        # 가장 싼 물품 가격 구하기(물품 정보를 리스트로 저장해서 min을 못 씀)
        cnt = 0
        price_min = product.price
        for i, p in enumerate(machine.product(), start=1):
            price_min = min(price_min, p.price)
        if 0 < machine.money < price_min:
            money_out()


def call_admin():
    print('관리자에게 연락하십시오.')


# 파일 로드
try:
    machine = load_product()
except FileNotFoundError:
    call_admin()
else:
    # 데이터가 없는 경우
    if len(machine.product()) == 0:
        call_admin()

# 호갱 모드로 진입
customer_mode()
